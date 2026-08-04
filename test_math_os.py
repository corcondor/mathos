import unittest

from math_os_prototype.arithmetic_nl import detect_arithmetic_nl_problem
from math_os_prototype.case_frame_parser import parse_case_frames
from math_os_prototype.category_semantics import compile_typed_semantic_graph, run_verifier_gate
from math_os_prototype.container_geometry import detect_container_problem, solve_container_problem
from math_os_prototype.domain_registry import DomainRegistry, run_domain_benchmark
from math_os_prototype.formal_language import compile_formal_ir
from math_os_prototype.geometry_dsl import parse_geometry_dsl, run_geometry_dsl
from math_os_prototype.geometry_nl import convert_geometry_nl
from math_os_prototype.generalization_benchmark import (
    generate_generalization_cases,
    generate_same_structure_pairs,
    run_generalization_benchmark,
)
from math_os_prototype.latex_frontend import parse_latex_problem, split_tex_text_math
from math_os_prototype.lift_lifter import run_lift_lifter_experiment
from math_os_prototype.math_os import ProblemCompiler, TinyRouter, ToolExecutor, run_pipeline
from math_os_prototype.math_search import run_math_search
from math_os_prototype.quantity_reasoner import solve_quantity_reasoning_problem
from math_os_prototype.reasoning_pipeline import run_reasoning_pipeline
from math_os_prototype.retriever import HybridRetriever, QueryBuilder
from math_os_prototype.solution_step_parser import SolutionStepParser
from math_os_prototype.step_verifier import StepVerifier
from math_os_prototype.structural_parser import analyze_structure
from math_os_prototype.theory_atlas import canonical_graph_signature, compare_lift_structures
from math_os_prototype.tool_adapters import ToolRegistry, wolfram_code_for_geometry
from math_os_prototype.typed_definition_kernel import LEXICON, compile_typed_definition_ir
from math_os_prototype.web_app import extract_answer_from_pipeline_data, solve_request_payload
from math_os_prototype.web_solution_fetcher import extract_stackexchange_question_id


class MathOsPrototypeTest(unittest.TestCase):
    def test_arithmetic_nl_compiles_reusable_syntax(self):
        problem = (
            "Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning "
            "and bakes muffins for her friends every day with four. She sells the remainder "
            "at the farmers' market daily for $2 per fresh duck egg."
        )
        parsed = detect_arithmetic_nl_problem(problem)
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed.intent, "remainder_sale")
        self.assertEqual(parsed.expression, "(16-3-4)*2")

    def test_full_pipeline_solves_arithmetic_nl_without_specialized_adapter(self):
        result = solve_request_payload(
            {
                "problem": "What is the positive difference between $120\\%$ of 30 and $130\\%$ of 20?",
                "full_pipeline": True,
            }
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "10")
        self.assertEqual(result["data"]["parser"]["intent"], "arithmetic_nl_percent_difference")

    def test_full_pipeline_solves_public_word_problem_syntax(self):
        result = solve_request_payload(
            {
                "problem": (
                    "John drives for 3 hours at a speed of 60 mph and then turns around. "
                    "He tries to get home in 4 hours but spends the first 2 hours in standstill traffic. "
                    "He spends the next half-hour driving at a speed of 30mph, before being able to drive "
                    "the remaining time of the 4 hours going at 80 mph. How far is he from home?"
                ),
                "full_pipeline": True,
            }
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "45")

    def test_arithmetic_nl_handles_math_benchmark_syntax(self):
        asymptote = solve_request_payload(
            {
                "problem": r"How many vertical asymptotes does the graph of $y=\frac{2}{x^2+x-6}$ have?",
                "full_pipeline": True,
            }
        )
        dice = solve_request_payload(
            {
                "problem": r"$n$ fair 6-sided dice are simultaneously rolled. The probability that exactly two of them show a number other than 1 is $\frac{25}{216}$. Find $n$.",
                "full_pipeline": True,
            }
        )
        self.assertEqual(asymptote["answer"], "2")
        self.assertEqual(dice["answer"], "4")

    def test_surface_morphism_adapters_are_opt_in(self):
        text = "What is the 100th term of the arithmetic sequence 6 10 14?"
        self.assertIsNone(detect_arithmetic_nl_problem(text))
        enabled = detect_arithmetic_nl_problem(text, allow_surface_morphisms=True)
        self.assertIsNotNone(enabled)
        self.assertEqual(enabled.intent, "allfield_arithmetic_sequence_nth_term")

        cold = run_reasoning_pipeline(text)
        self.assertNotEqual(cold.parser["intent"], "arithmetic_nl_allfield_arithmetic_sequence_nth_term")
        specialized = run_reasoning_pipeline(text, allow_specialized=True)
        self.assertEqual(specialized.parser["intent"], "arithmetic_nl_allfield_arithmetic_sequence_nth_term")

    def test_semantic_graph_lifts_solution_parts_as_morphisms(self):
        sequence = compile_typed_semantic_graph(
            "What is the 100th term of the arithmetic sequence whose first term is 6 and second term is 10?"
        )
        sequence_morphisms = {item.name for item in sequence.morphisms}
        sequence_queries = {item.target for item in sequence.queries}
        self.assertIn("ArithmeticProgression", sequence_morphisms)
        self.assertIn("NthTerm", sequence_morphisms)
        self.assertIn("NthTerm(seq,100)", sequence_queries)

        geometry = compile_typed_semantic_graph("Find the distance from the origin to the point (3,4).")
        geometry_morphisms = {item.name for item in geometry.morphisms}
        geometry_queries = {item.target for item in geometry.queries}
        self.assertIn("Distance", geometry_morphisms)
        self.assertIn("Distance(O,P)", geometry_queries)

        midpoint = compile_typed_semantic_graph("Find the sum of the coordinates of the midpoint of (2,6) and (8,10).")
        midpoint_morphisms = {item.name for item in midpoint.morphisms}
        midpoint_queries = {item.target for item in midpoint.queries}
        self.assertIn("Midpoint", midpoint_morphisms)
        self.assertIn("CoordinateSum", midpoint_morphisms)
        self.assertIn("CoordinateSum(Midpoint(A,B))", midpoint_queries)

    def test_lift_certificates_define_same_structure(self):
        first = compile_typed_semantic_graph("What is the 100th term of the arithmetic sequence 6 10 14?")
        second = compile_typed_semantic_graph("Find the 50th term of the arithmetic sequence 2 5 8.")
        report = compare_lift_structures(first.lift_certificates, second.lift_certificates)
        self.assertTrue(report["same_structure"])
        self.assertTrue(any("discrete_affine_sequence.nth_term" in item for item in report["shared_signatures"]))

        distance_a = compile_typed_semantic_graph("Find the distance from the origin to the point (3,4).")
        distance_b = compile_typed_semantic_graph("Compute the distance from the origin to the point (5,12).")
        distance_report = compare_lift_structures(distance_a.lift_certificates, distance_b.lift_certificates)
        self.assertTrue(distance_report["same_structure"])
        self.assertTrue(any("inner_product_geometry.distance" in item for item in distance_report["shared_signatures"]))

        sequence_signature = canonical_graph_signature(first.lift_certificates)
        distance_signature = canonical_graph_signature(distance_a.lift_certificates)
        self.assertFalse(set(sequence_signature) & set(distance_signature))

    def test_generalization_benchmark_protocol_covers_required_axes(self):
        cases = generate_generalization_cases(seeds=1)
        pairs = generate_same_structure_pairs(cases)
        family_count = len({case.family_id for case in cases})
        self.assertGreaterEqual(family_count, 25)
        self.assertEqual(len(cases), family_count * 3)
        self.assertEqual(len(pairs), family_count * 2)
        self.assertEqual({case.transform for case in cases}, {"base", "surface", "numeric"})
        self.assertIn("held_out", {case.split for case in cases})

        result = run_generalization_benchmark(seeds=1, modes=["certified_lift_backend"])
        self.assertEqual(result["generated"]["case_count"], family_count * 3)
        self.assertEqual(result["generated"]["same_structure_pair_count"], family_count * 2)
        certified = result["modes"]["certified_lift_backend"]
        self.assertEqual(certified["lift_family_match_rate"], 1.0)
        self.assertEqual(certified["lift_certificate_pair_match_rate"], 1.0)

    def test_lift_lifter_learns_certificates_not_answers(self):
        result = run_lift_lifter_experiment(seeds=5)
        summary = result["seven_axis_summary"]
        self.assertEqual(summary["1_family_id"], 1.0)
        self.assertEqual(summary["2_morphism_chain"], 1.0)
        self.assertEqual(summary["3_constraint_skeleton"], 1.0)
        self.assertEqual(summary["4_query_signature"], 1.0)
        self.assertEqual(summary["5_backend_execution_success"], 1.0)
        self.assertEqual(summary["6_surface_numeric_same_structure"], 1.0)
        self.assertEqual(summary["7_negative_structure_not_confused"], 1.0)

    def test_case_frame_arithmetic_handles_public_word_problem_relations(self):
        breakeven = solve_request_payload(
            {
                "problem": (
                    "Carlos is planting a lemon tree. The tree will cost $90 to plant. "
                    "Each year it will grow 7 lemons, which he can sell for $1.5 each. "
                    "It costs $3 a year to water and feed the tree. How many years will it take "
                    "before he starts earning money on the lemon tree?"
                ),
                "full_pipeline": True,
            }
        )
        speed = solve_request_payload(
            {
                "problem": (
                    "Marissa is hiking a 12-mile trail. She took 1 hour to walk the first 4 miles, "
                    "then another hour to walk the next two miles. If she wants her average speed "
                    "to be 4 miles per hour, what speed (in miles per hour) does she need to walk "
                    "the remaining distance?"
                ),
                "full_pipeline": True,
            }
        )
        self.assertEqual(breakeven["answer"], "13")
        self.assertEqual(speed["answer"], "6")
        self.assertTrue(breakeven["data"]["parser"]["intent"].startswith("arithmetic_nl_case_frame_"))
        self.assertTrue(speed["data"]["parser"]["intent"].startswith("arithmetic_nl_case_frame_"))

    def test_arithmetic_nl_generic_state_updates(self):
        state = solve_request_payload(
            {
                "problem": "Paige had 11 songs on her mp3 player. If she deleted 9 old songs from it and then added 8 new songs, how many songs does she have on her mp3 player?",
                "full_pipeline": True,
            }
        )
        remaining_time = solve_request_payload(
            {
                "problem": "A painter needed to paint 12 rooms in a building. Each room takes 7 hours to paint. If he already painted 5 rooms, how much longer will he take to paint the rest?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(state["answer"], "10")
        self.assertEqual(remaining_time["answer"], "49")

    def test_arithmetic_nl_tracks_target_objects(self):
        cookies = solve_request_payload(
            {
                "problem": "Paco had 9 sweet cookies and 6 salty cookies. He ate 36 sweet cookies and 3 salty cookies. How many salty cookies did Paco have left?",
                "full_pipeline": True,
            }
        )
        coops = solve_request_payload(
            {
                "problem": "Ben counted a total of 9 chicken coops and Daniel said that there are 60 chickens in one coop. How many chickens do they have in total?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(cookies["answer"], "3")
        self.assertEqual(coops["answer"], "540")

    def test_quantity_reasoner_handles_complement_counts_and_pronouns(self):
        recycled = solve_request_payload(
            {
                "problem": "Megan earned 8 points for each bag of cans she recycled. If she had 14 bags, but didn't recycle 5 of them, how many points would she have earned?",
                "full_pipeline": True,
            }
        )
        books = solve_request_payload(
            {
                "problem": "Tom had 5 books. If he sold 4 of them and used the money he earned to buy 38 new books, how many books would Tom have?",
                "full_pipeline": True,
            }
        )
        tips = solve_request_payload(
            {
                "problem": "At lunch a waiter had 7 customers and 5 of them didn't leave a tip. If he got $3 each from the ones who did tip, how much money did he earn?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(recycled["answer"], "72")
        self.assertEqual(books["answer"], "39")
        self.assertEqual(tips["answer"], "6")

    def test_quantity_reasoner_distinguishes_containers_from_products(self):
        folders = solve_request_payload(
            {
                "problem": "Nancy had 80 files on her computer. She deleted 31 of them and put the rest into folders with 7 files in each one. How many folders did Nancy end up with?",
                "full_pipeline": True,
            }
        )
        quarters = solve_request_payload(
            {
                "problem": "Jason had 49 quarters in his bank. His dad gave him 25 more quarters. How many quarters does he have now?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(folders["answer"], "7")
        self.assertEqual(quarters["answer"], "74")

    def test_quantity_reasoner_builds_structural_equation_candidates(self):
        gain_loss = solve_request_payload(
            {
                "problem": "Dave had 21 apps on his phone. He added 89 new apps. After deleting some he had 24 left. How many more apps did he add than he deleted?",
                "full_pipeline": True,
            }
        )
        category_diff = solve_request_payload(
            {
                "problem": "In a school there are 362 boys and 257 girls. 403 more girls joined the school. How many more girls than boys does the school have?",
                "full_pipeline": True,
            }
        )
        per_unit_diff = solve_request_payload(
            {
                "problem": "They have 14 chairs for each set of table. If they have 9 sets of tables How many more chairs than tables do they have?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(gain_loss["answer"], "3")
        self.assertEqual(category_diff["answer"], "298")
        self.assertEqual(per_unit_diff["answer"], "117")

    def test_quantity_reasoner_handles_time_cost_and_partitions(self):
        time_diff = solve_request_payload(
            {
                "problem": "Julia played tag with 9 kids on monday, 7 kids on tuesday and 96 kids on wednesday. How many more kids did she play with on monday than on tuesday?",
                "full_pipeline": True,
            }
        )
        breakfast = solve_request_payload(
            {
                "problem": "Ron and Chanarong had breakfast at a cafe. Muffins cost $2 each, and fruit cups cost $2 each. Ron had 1 muffin and 2 fruit cups. Chanarong had 1 muffin and 2 fruit cups. How much did their breakfast cost?",
                "full_pipeline": True,
            }
        )
        groups = solve_request_payload(
            {
                "problem": "There are 56 students in the class. The teacher wants to split them into two groups. The first group has 24 students. How many more students will there be in the second group?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(time_diff["answer"], "2")
        self.assertEqual(breakfast["answer"], "12")
        self.assertEqual(groups["answer"], "8")

    def test_quantity_reasoner_handles_partitions_capacity_and_initial_gain(self):
        split = solve_request_payload(
            {
                "problem": "At a company picnic 23 managers and 7 employees decided to start a game of volleyball. If they split into 6 teams how many people would be on each team?",
                "full_pipeline": True,
            }
        )
        buses = solve_request_payload(
            {
                "problem": "The school has 67 classrooms. There are 66 students in each classroom. If there are 6 seats on each school bus How many buses are needed?",
                "full_pipeline": True,
            }
        )
        initial = solve_request_payload(
            {
                "problem": "Tera had some mango. Becky gave him 7 more. Now Tera has 31 mango. How many mango did Tera have initially?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(split["answer"], "5")
        self.assertEqual(buses["answer"], "737")
        self.assertEqual(initial["answer"], "24")

    def test_quantity_reasoner_handles_complement_partition_and_local_unit_labels(self):
        complement = solve_request_payload(
            {
                "problem": "John earned 8 dollars for each lawn he mowed. If he had 15 lawns to mow, but forgot to mow 7 of them, how much money did he actually earn?",
                "full_pipeline": True,
            }
        )
        remaining = solve_request_payload(
            {
                "problem": "Tiffany baked 8 brownies, but needed 17 total for her party. If she used 8 cups of flour on each one, how much cups of flour does she still need?",
                "full_pipeline": True,
            }
        )
        label_rate = solve_request_payload(
            {
                "problem": "The shop makes $115 off each jersey and $25 off each t-shirt. How much more does a jersey cost than a t-shirt?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(complement["answer"], "64")
        self.assertEqual(remaining["answer"], "72")
        self.assertEqual(label_rate["answer"], "90")

    def test_quantity_reasoner_emits_logic_level_semantics(self):
        result = solve_quantity_reasoning_problem(
            "The school has 67 classrooms. There are 66 students in each classroom. "
            "If there are 6 seats on each school bus How many buses are needed?"
        )
        self.assertIsNotNone(result)
        self.assertEqual(result.answer_exact, "737")
        self.assertEqual(result.semantic_model["output_sort"]["base"], "Count")
        self.assertEqual(result.semantic_model["output_sort"]["obj"], "bus")
        self.assertIn("(typed answer (Count bus))", result.semantic_model["obligations"])
        self.assertIn("(Rate student classroom)", result.semantic_model["best_sequent"])
        self.assertIn("(Rate seat bus)", result.semantic_model["best_sequent"])
        payload = solve_request_payload(
            {
                "problem": "The school has 67 classrooms. There are 66 students in each classroom. If there are 6 seats on each school bus How many buses are needed?",
                "full_pipeline": True,
            }
        )
        semantic_model = payload["data"]["parser"]["givens"]["arithmetic_problem"]["metadata"]["semantic_model"]
        self.assertEqual(semantic_model["output_sort"]["obj"], "bus")

    def test_quantity_reasoner_handles_generic_state_rate_and_selection(self):
        per_day = solve_request_payload(
            {
                "problem": "The ring toss game made the same amount of money each day. In total in 5 days they earned 165 dollars. How much did they make per day?",
                "full_pipeline": True,
            }
        )
        target_sum = solve_request_payload(
            {
                "problem": "Allan brought 3 balloons and 20 balls while Jake brought 5 balloons and 59 balls to the park. How many balloons did Allan and Jake have in the park?",
                "full_pipeline": True,
            }
        )
        earlier = solve_request_payload(
            {
                "problem": "After finding some bottle caps at the park Danny has 32 bottle caps. If he had 25 bottle caps earlier How many bottle caps did he find?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(per_day["answer"], "33")
        self.assertEqual(target_sum["answer"], "8")
        self.assertEqual(earlier["answer"], "7")

    def test_quantity_reasoner_composes_a_typed_rate_chain(self):
        result = solve_quantity_reasoning_problem(
            "A classroom has a whiteboard shared by 4 teachers. "
            "Each teacher has 2 lessons per day. The whiteboard is cleaned "
            "3 times per lesson. How many times is it cleaned in a day?"
        )
        self.assertIsNotNone(result)
        self.assertEqual(result.answer_exact, "24")
        self.assertEqual(result.semantic_model["best_candidate_kind"], "typed_rate_chain")
        self.assertIn("(Rate lesson teacher)", result.semantic_model["best_sequent"])
        self.assertIn("(Rate time lesson)", result.semantic_model["best_sequent"])

    def test_quantity_reasoner_merges_parallel_rate_branches_before_observation(self):
        per_basket = solve_quantity_reasoning_problem(
            "There are 65 baskets of peaches. Each basket has 7 red peaches and 3 green peaches. "
            "How many peaches are in each basket?"
        )
        total = solve_quantity_reasoning_problem(
            "There are 11 baskets of peaches. Each basket has 10 red peaches and 18 green peaches. "
            "How many peaches are in the baskets altogether?"
        )
        self.assertEqual(per_basket.answer_exact, "10")
        self.assertEqual(total.answer_exact, "308")
        self.assertIn("parallel_rate_merge", per_basket.candidates[0]["checks"])

    def test_quantity_reasoner_composes_affine_relations_without_name_or_number_templates(self):
        first = solve_quantity_reasoning_problem(
            "Amy made 20 more friends than Lily. Lily made 50 friends. "
            "How many friends do Lily and Amy have together?"
        )
        changed = solve_quantity_reasoning_problem(
            "Nora made 7 more friends than Mei. Mei made 12 friends. "
            "How many friends do Mei and Nora have together?"
        )
        self.assertEqual(first.answer_exact, "120")
        self.assertEqual(changed.answer_exact, "31")
        self.assertEqual(first.semantic_model["best_candidate_kind"], "affine_entity_relation")

    def test_quantity_reasoner_composes_fractional_allocation_and_conservation(self):
        first = solve_quantity_reasoning_problem(
            "Two girls each got 1/6 of the 24 liters of water. Then a boy got 6 liters. "
            "How many liters were left?"
        )
        changed = solve_quantity_reasoning_problem(
            "Three teams each received 1/8 of the 40 boxes. Then a club took 5 boxes. "
            "How many boxes were left?"
        )
        self.assertEqual(first.answer_exact, "10")
        self.assertEqual(changed.answer_exact, "20")
        self.assertEqual(first.semantic_model["best_candidate_kind"], "fractional_each_allocation")

    def test_quantity_reasoner_does_not_treat_dimensions_or_percent_as_counts(self):
        result = solve_quantity_reasoning_problem(
            "Lumber prices rose 50%. There are ten 2 x 4 x 10 boards costing $10 each "
            "and five 4 x 4 x 10 boards costing $16 each. How much profit is made?"
        )
        self.assertIsNone(result)

    def test_quantity_reasoner_handles_unit_price_and_group_inversion(self):
        unit_price = solve_request_payload(
            {
                "problem": "The shop made $51 from selling 3 t-shirt. What is the cost of each t-shirt?",
                "full_pipeline": True,
            }
        )
        boys = solve_request_payload(
            {
                "problem": "Haley has 10 marbles and she gave 5 marbles to each boy. How many boys did she give the marbles to?",
                "full_pipeline": True,
            }
        )
        groups = solve_request_payload(
            {
                "problem": "Rebecca wants to split eggs into 3 groups. Rebecca has 4 marbles and 15 eggs. How many eggs will each group have?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(unit_price["answer"], "17")
        self.assertEqual(boys["answer"], "2")
        self.assertEqual(groups["answer"], "5")

    def test_quantity_reasoner_handles_remaining_goal_forms(self):
        pictures = solve_request_payload(
            {
                "problem": "Nancy took 49 pictures at the zoo and 8 at the museum. If she later deleted 38 of the pictures, how many pictures did she still have?",
                "full_pipeline": True,
            }
        )
        cakes = solve_request_payload(
            {
                "problem": "Baker made 155 cakes. If his friend bought 140 cakes from him How many cakes would baker still have?",
                "full_pipeline": True,
            }
        )
        needed = solve_request_payload(
            {
                "problem": "She needs 125 rocks to complete the border. She has 64 rocks. How many more rocks does she need?",
                "full_pipeline": True,
            }
        )
        self.assertEqual(pictures["answer"], "19")
        self.assertEqual(cakes["answer"], "15")
        self.assertEqual(needed["answer"], "61")

    def test_typed_definition_kernel_covers_core_vocabulary(self):
        surfaces = {surface for entry in LEXICON for surface in entry.surfaces}
        for word in (
            "点",
            "直線",
            "曲線",
            "円",
            "三角形",
            "正三角形",
            "重心",
            "接線",
            "交点",
            "軌跡",
            "領域",
            "面積",
            "最大値",
            "整数",
            "素数",
            "確率",
            "期待値",
            "すべて",
            "存在する",
            "満たす",
            "求めよ",
            "示せ",
            "かつ",
            "ならば",
        ):
            self.assertIn(word, surfaces)

    def test_japanese_case_frame_parser_reads_particles_as_slots(self):
        ir = parse_case_frames(r"任意の整数 n に対して、n^2 が偶数ならば n も偶数であることを示せ。")
        relations = [frame.relation for frame in ir.frames]
        self.assertIn("Forall", relations)
        self.assertIn("Prove", relations)

        locus = parse_case_frames(r"点 P が曲線 C 上にあるとき、P の軌跡を求めよ。")
        logic = [frame.logic for frame in locus.frames]
        self.assertIn("(On \"点 P\" \"曲線 C\")", logic)
        self.assertTrue(any(item.startswith("(Query") for item in logic))

    def test_typed_definition_ir_exposes_case_frames(self):
        ir = compile_typed_definition_ir(r"実数 x が x^2-5*x+6=0 を満たすとき、x を求めよ。")
        self.assertIsNotNone(ir.case_frames)
        self.assertIn("Satisfies", [frame["relation"] for frame in ir.case_frames["frames"]])

    def test_typed_declarations_infer_function_application(self):
        ir = compile_typed_definition_ir(
            r"関数 $f(x),g(x)$ が $\int_0^1 f(x)g(x)dx=1$ を満たすとき一組求めよ。"
        )
        declarations = {item["name"]: item["type"] for item in ir.declarations}
        self.assertEqual(declarations["f"], "Function(Real, Real)")
        self.assertEqual(declarations["g"], "Function(Real, Real)")
        self.assertEqual(declarations["x"], "Real")

    def test_typed_declarations_infer_complex_sequence_from_definition(self):
        text = r"$n$を正の整数とする。複素数平面上の点 $z_n=n+i$ を考える。"
        ir = compile_typed_definition_ir(text)
        declarations = {item["name"]: item["type"] for item in ir.declarations}
        self.assertEqual(declarations["n"], "Integer")
        self.assertEqual(declarations["z_n"], "Sequence(Complex)")

        graph = compile_typed_semantic_graph(text, typed_definition_ir=ir.to_dict())
        objects = {item.name: item.sort for item in graph.objects}
        self.assertEqual(objects["z_n"], "Sequence(Complex)")
        self.assertTrue(any(item.name == "Complex" for item in graph.sorts))

    def test_proof_representation_changes_compile_as_typed_morphisms(self):
        text = (
            r"$x=y-a/3$ とおく。$g'(y)$ の符号から単調増加を示す。"
            r"判別式を調べ、共役な根を得る。係数比較により条件を求める。"
        )
        graph = compile_typed_semantic_graph(text)
        names = {item.name for item in graph.morphisms}
        self.assertTrue(
            {
                "PolynomialTranslation",
                "Differentiation",
                "MonotonicityTest",
                "Discriminant",
                "ComplexConjugation",
                "CoefficientComparison",
            }
            <= names
        )

    def test_typed_definition_kernel_generalizes_regular_polygon(self):
        ir = compile_typed_definition_ir(
            r"$\text{曲線 }$y=x^3−2x"
            r"$\text{ 上の3点を頂点とする正三角形の重心の軌跡が囲む部分の面積を求めよ }$"
        )
        self.assertEqual(ir.status, "type_checked")
        self.assertIn("RegularPolygon", [entry["canonical"] for entry in ir.definitions_used])
        self.assertIn({"name": "P", "type": "Fin(3) -> Point2"}, ir.declarations)
        self.assertEqual(ir.query["kind"], "compute")
        self.assertIn("Area(BoundedRegion(Locus", ir.query["expression"])
        self.assertIn("real_closed_fields", [item["theory"] for item in ir.backend_obligations])

    def test_typed_definition_kernel_does_not_promote_japanese_particles_to_logic(self):
        maximum = compile_typed_definition_ir(
            "正十二面体から3点を取るとき、三角形の面積の最大値を求めよ。"
        )
        sine = compile_typed_definition_ir(r"$\sin x=0$ を満たす実数を求めよ。")
        assertion = compile_typed_definition_ir("nは整数である。")

        maximum_names = {entry["canonical"] for entry in maximum.definitions_used}
        sine_names = {entry["canonical"] for entry in sine.definitions_used}
        assertion_names = {entry["canonical"] for entry in assertion.definitions_used}
        self.assertNotIn("Decide", maximum_names)
        self.assertEqual(maximum.query["target"], "maximum")
        self.assertNotIn("Member", sine_names)
        self.assertNotIn("Exists", assertion_names)

    def test_typed_definition_kernel_has_first_class_measure_and_limit_queries(self):
        limit_ir = compile_typed_definition_ir(r"$\lim_{n\to\infty} a_n$ を求めよ。")
        volume_ir = compile_typed_definition_ir("立体Kの体積を求めよ。")
        correlation_ir = compile_typed_definition_ir("確率変数X,Yの相関係数を求めよ。")

        self.assertEqual(limit_ir.query["expression"], "Limit(target)")
        self.assertEqual(volume_ir.query["expression"], "Volume(target_region)")
        self.assertEqual(correlation_ir.query["expression"], "Correlation(X,Y)")

    def test_correlation_is_compiled_through_centered_inner_product(self):
        ir = compile_typed_definition_ir(
            "確率変数X,Yの共分散と相関係数を求めよ。"
        )
        names = {item["canonical"] for item in ir.definitions_used}
        self.assertTrue(
            {
                "Center",
                "Covariance",
                "InnerProduct",
                "Norm",
                "NormalizedInnerProduct",
                "Correlation",
            }
            <= names
        )

    def test_inner_product_structures_receive_specific_lift_certificates(self):
        examples = {
            (
                "行列A,Bのフロベニウス内積を求めよ。",
                "linear_algebra.frobenius_pairing",
            ),
            (
                "実内積空間でベクトルvの部分空間Sへの直交射影を求めよ。",
                "linear_algebra.orthogonal_projection",
            ),
            (
                "正定値行列Qによる二次形式の最小値を求めよ。",
                "optimization.positive_definite_quadratic",
            ),
            (
                "正規化内積のnから無限大における極限を求めよ。",
                "real_analysis.normalized_inner_product_limit",
            ),
            (
                "弱定常過程Xの相関関数を求めよ。",
                "probability.autocorrelation_function",
            ),
        }
        for text, expected in examples:
            typed = compile_typed_definition_ir(text)
            graph = compile_typed_semantic_graph(
                text,
                typed_definition_ir=typed.to_dict(),
            )
            ids = {
                item.family_id
                for item in graph.lift_certificates
                if item.admissible
            }
            self.assertIn(expected, ids)

    def test_category_semantic_graph_lifts_quantity_observables(self):
        text = "Jake brought 6 balloons. Jake then bought 3 more balloons. How many balloons did Jake bring?"
        graph = compile_typed_semantic_graph(text)
        self.assertEqual(graph.status, "type_checked")
        self.assertIn("Observable", [sort.name for sort in graph.sorts])
        self.assertIn("Count[balloon]", [sort.name for sort in graph.sorts])
        self.assertTrue(any(morphism.kind == "observable" for morphism in graph.morphisms))
        self.assertTrue(any(query.sort == "Count[balloon]" for query in graph.queries))
        gate = run_verifier_gate(graph, answer="9")
        self.assertEqual(gate.status, "accepted")
        self.assertIn("morphism_sorts_resolved", gate.checks)

    def test_pure_tex_math_does_not_create_spurious_quantity_observables(self):
        graph = compile_typed_semantic_graph(
            r"$\displaystyle\lim_{n\to\infty}\frac{1}{n}=0$ を示せ。"
        )
        morphism_names = {morphism.name for morphism in graph.morphisms}

        self.assertNotIn("observe_dollar", morphism_names)
        self.assertNotIn("observe_frac", morphism_names)
        self.assertNotIn("observe_n", morphism_names)
        self.assertFalse(any(name.startswith("observe_") for name in morphism_names))

        japanese_tex = compile_typed_semantic_graph(
            r"1から$n$までのカードが1枚ずつあり、2枚を引くときの相関係数を求めよ。"
        )
        japanese_names = {morphism.name for morphism in japanese_tex.morphisms}
        self.assertNotIn("observe_n", japanese_names)
        self.assertNotIn("observe_quantity", japanese_names)

    def test_category_semantic_graph_lifts_geometry_as_objects_and_morphisms(self):
        text = r"$\text{曲線 }$y=x^3−2x$\text{ 上の3点を頂点とする正三角形の重心の軌跡が囲む部分の面積を求めよ }$"
        typed = compile_typed_definition_ir(text)
        formal = compile_formal_ir(text)
        graph = compile_typed_semantic_graph(
            text,
            typed_definition_ir=typed.to_dict(),
            formal_ir=formal.to_dict(),
        )
        morphism_names = {morphism.name for morphism in graph.morphisms}
        self.assertIn("RegularPolygon", morphism_names)
        self.assertIn("Centroid", morphism_names)
        self.assertIn("Area", morphism_names)
        self.assertTrue(any(query.kind == "compute" for query in graph.queries))
        self.assertTrue(any("Centroid" in constraint.expression for constraint in graph.constraints))
        certificate_ids = {item.family_id for item in graph.lift_certificates if item.admissible}
        self.assertIn("measure_geometry.locus_area", certificate_ids)

    def test_category_semantic_graph_certifies_abstract_limit_and_prime_queries(self):
        limit_text = r"$\lim_{n\to\infty} a_n$ を求めよ。"
        limit_typed = compile_typed_definition_ir(limit_text)
        limit_graph = compile_typed_semantic_graph(
            limit_text,
            typed_definition_ir=limit_typed.to_dict(),
        )
        prime_text = "素数p,qについて条件を満たす組をすべて求めよ。"
        prime_typed = compile_typed_definition_ir(prime_text)
        prime_graph = compile_typed_semantic_graph(
            prime_text,
            typed_definition_ir=prime_typed.to_dict(),
        )

        limit_ids = {item.family_id for item in limit_graph.lift_certificates if item.admissible}
        prime_ids = {item.family_id for item in prime_graph.lift_certificates if item.admissible}
        self.assertIn("real_analysis.limit_observable", limit_ids)
        self.assertIn("elementary_number_theory.prime_constraint_query", prime_ids)

    def test_full_pipeline_exposes_typed_definition_ir(self):
        result = solve_request_payload(
            {
                "problem": r"素数 p に対して p>1 を示せ。",
                "full_pipeline": True,
            }
        )
        self.assertTrue(result["ok"])
        typed_ir = result["data"]["typed_definition_ir"]
        self.assertIn("Prime", [entry["canonical"] for entry in typed_ir["definitions_used"]])
        self.assertIn("Prove", [entry["canonical"] for entry in typed_ir["definitions_used"]])
        self.assertIn("TypedKernel:", result["reply"])
        self.assertIn("semantic_graph", result["data"])
        self.assertIn("constraint_ir", result["data"])
        self.assertIn("verifier_gate", result["data"])
        self.assertIn("SemanticGraph:", result["reply"])
        self.assertIn("VerifierGate:", result["reply"])

    def test_rejected_verifier_gate_blocks_answer_extraction(self):
        data = {
            "verifier_gate": {"status": "rejected", "rejection": "bad semantic sort"},
            "tool_execution": {
                "tool_calls": [
                    {
                        "name": "mock.solver",
                        "status": "executed",
                        "result": {"answer_exact": "999"},
                    }
                ]
            },
        }
        self.assertIsNone(extract_answer_from_pipeline_data(data))

    def test_domain_registry_classifies_broad_domains(self):
        registry = DomainRegistry()
        self.assertEqual(registry.analyze("素数 p に対して a^p ≡ a mod p を示せ。").domain, "number_theory")
        self.assertEqual(registry.analyze("グラフ G の頂点彩色数を求めよ。").domain, "graph_theory")
        self.assertEqual(registry.analyze("サイコロを2回振るとき和が7になる確率を求めよ。").domain, "probability")

    def test_domain_registry_normalizes_japanese_query_vocabulary(self):
        registry = DomainRegistry()
        region = registry.analyze("点Pが動くとき円の通過領域を求めよ。")
        locus = registry.analyze("点Hの軌跡を求めよ。")
        proof = registry.analyze("素数pについて合同式を示せ。")

        self.assertEqual(region.operation, "passing_region")
        self.assertEqual(locus.operation, "locus")
        self.assertEqual(proof.domain, "number_theory")
        self.assertNotEqual(proof.domain, "inequalities")

    def test_domain_benchmark_accuracy(self):
        result = run_domain_benchmark()
        self.assertGreaterEqual(result["accuracy"], 0.9)
        self.assertEqual(result["total"], 18)

    def test_full_pipeline_includes_domain_ir_for_unregistered_problem(self):
        result = run_reasoning_pipeline("サイコロを2回振るとき和が7になる確率を求めよ。")
        self.assertEqual(result.domain_ir["domain"], "probability")
        self.assertEqual(result.parser["domain"], "probability")
        self.assertIn("probability_domain_plan", [item["name"] for item in result.strategies])
        self.assertEqual(result.verification["status"], "partial")
        self.assertTrue(result.parser["cold_mode"])
        self.assertIn("structural_ir", result.to_json())

    def test_cold_mode_does_not_use_specialized_benchmark_adapter(self):
        text = r"$m$週間と$n!$秒が等しくなる非負整数の組($m,n$)をすべて求めよ."
        result = solve_request_payload({"problem": text, "full_pipeline": True})
        self.assertTrue(result["ok"])
        self.assertTrue(result["data"]["parser"]["cold_mode"])
        self.assertNotEqual(
            result["data"]["tool_execution"]["tool_calls"][0]["name"] if result["data"]["tool_execution"]["tool_calls"] else "",
            "number_theory.factorial_weeks",
        )

    def test_structural_parser_and_math_search_emit_generic_experiments(self):
        structure = analyze_structure("正の整数 n について n^2 = 9 を満たすものをすべて求めよ。")
        search = run_math_search(structure, external_tools=False)
        action_names = [action["name"] for action in search.actions]
        self.assertIn("generic_wolfram_experiment", action_names)
        self.assertIn("integer_model_search", structure.tool_affordances)
        self.assertEqual(search.answer, "['3']")

    def test_full_pipeline_returns_solution_graph_from_generic_search(self):
        result = solve_request_payload({"problem": "正の整数 n について n^2 = 9 を満たすものをすべて求めよ。", "full_pipeline": True})
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "['3']")
        self.assertEqual(result["data"]["solution_graph"]["status"], "verified_candidate")
        self.assertIn("formal_ir", result["data"])

    def test_generic_math_search_evaluates_expression_under_constraints(self):
        result = solve_request_payload(
            {
                "problem": r"実数 $x,y$ が $x+y=5$ かつ $xy=6$ を満たすとき、$x^2+y^2$ を求めよ。",
                "full_pipeline": True,
            }
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "13")
        action_names = [action["name"] for action in result["data"]["math_search"]["actions"]]
        self.assertIn("generic_sympy_value_from_constraints", action_names)

    def test_generic_counterexample_respects_assumptions(self):
        result = solve_request_payload({"problem": "x>0 のとき x^2 < x を示せ。", "full_pipeline": True})
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "{'x': 1}")

    def test_generic_quadratic_existence_range(self):
        result = solve_request_payload(
            {
                "problem": r"実数 $x$ が $x^2-a*x+1=0$ を満たすような実数 $a$ の範囲を求めよ。",
                "full_pipeline": True,
            }
        )
        self.assertTrue(result["ok"])
        self.assertIn("a <= -2", result["answer"])
        self.assertIn("2 <= a", result["answer"])

    def test_generic_tex_limit_integral_and_factor(self):
        limit_result = solve_request_payload(
            {"problem": r"$\lim_{x\to0} \frac{\sin x}{x}$ を求めよ。", "full_pipeline": True}
        )
        integral_result = solve_request_payload(
            {"problem": r"$\int_0^1 x^2 dx$ を求めよ。", "full_pipeline": True}
        )
        factor_result = solve_request_payload(
            {"problem": r"$x^2+2x+1$ を因数分解せよ。", "full_pipeline": True}
        )
        self.assertEqual(limit_result["answer"], "1")
        self.assertEqual(integral_result["answer"], "1/3")
        self.assertEqual(factor_result["answer"], "(x + 1)**2")

    def test_generic_linear_system_derivative_and_dice_probability(self):
        system_result = solve_request_payload(
            {"problem": r"連立方程式 $x+y=5$, $x-y=1$ を解け。", "full_pipeline": True}
        )
        derivative_result = solve_request_payload(
            {"problem": r"$x^3+2x$ を $x$ で微分せよ。", "full_pipeline": True}
        )
        probability_result = solve_request_payload(
            {"problem": "サイコロを2回振るとき和が7になる確率を求めよ。", "full_pipeline": True}
        )
        self.assertIn("'x': '3'", system_result["answer"])
        self.assertIn("'y': '2'", system_result["answer"])
        self.assertEqual(derivative_result["answer"], "3*x**2 + 2")
        self.assertEqual(probability_result["answer"], "1/6")

    def test_generic_matrix_combinatorics_optimization_complex_and_remainder(self):
        determinant_result = solve_request_payload(
            {"problem": "行列 [[1,2],[3,4]] の行列式を求めよ。", "full_pipeline": True}
        )
        combination_result = solve_request_payload(
            {"problem": "5人から2人を選ぶ方法は何通りか。", "full_pipeline": True}
        )
        minimum_result = solve_request_payload(
            {"problem": r"実数 $x$ に対して $x^2-4*x+5$ の最小値を求めよ。", "full_pipeline": True}
        )
        complex_result = solve_request_payload(
            {"problem": r"複素数 $z=3+4i$ の絶対値を求めよ。", "full_pipeline": True}
        )
        remainder_result = solve_request_payload(
            {"problem": r"$2^10$ を $7$ で割った余りを求めよ。", "full_pipeline": True}
        )
        trig_result = solve_request_payload(
            {"problem": r"$\sin x=0$ を解け。", "full_pipeline": True}
        )
        self.assertEqual(determinant_result["answer"], "-2")
        self.assertEqual(combination_result["answer"], "10")
        self.assertEqual(minimum_result["answer"], "1")
        self.assertEqual(complex_result["answer"], "5")
        self.assertEqual(remainder_result["answer"], "2")
        self.assertEqual(trig_result["answer"], "['0', 'pi']")

    def test_long_japanese_logic_and_formal_ir(self):
        value_result = solve_request_payload(
            {
                "problem": "実数 x,y は、和が 5 で積が 6 である。さらに x<y とする。このとき x^2+y^2 の値を求めよ。",
                "full_pipeline": True,
            }
        )
        chain_result = solve_request_payload(
            {"problem": r"実数 x が $0<x<1$ を満たすとき、$x^2<x$ を示せ。", "full_pipeline": True}
        )
        condition_result = solve_request_payload(
            {
                "problem": r"実数 a について、すべての実数 x に対して $x^2+a*x+1>0$ が成り立つための a の必要十分条件を求めよ。",
                "full_pipeline": True,
            }
        )
        region_result = solve_request_payload(
            {
                "problem": r"t を実数全体にわたって動かす。各 t に対して曲線 C_t: $y=t*x-t^2$ を考える。このとき、少なくとも一つの t に対して点 (x,y) が C_t 上にあるような点全体の領域を求めよ。",
                "full_pipeline": True,
            }
        )
        predicate_formal = compile_formal_ir("正の整数 n について、n^2 が偶数ならば n も偶数であることを示せ。")
        predicate_result = solve_request_payload(
            {"problem": "正の整数 n について、n^2 が偶数ならば n も偶数であることを示せ。", "full_pipeline": True}
        )
        self.assertEqual(value_result["answer"], "13")
        self.assertEqual(chain_result["answer"], "proved")
        self.assertEqual(condition_result["answer"], "(-2 < a) & (a < 2)")
        self.assertEqual(region_result["answer"], "y <= x**2/4")
        self.assertEqual(predicate_result["answer"], "proved")
        self.assertIn("(exists ((t Real))", region_result["data"]["formal_ir"]["goal"])
        self.assertIn("(implies (even (^ n 2)) (even n))", predicate_formal.goal)
        action_names = [action["name"] for action in predicate_result["data"]["math_search"]["actions"]]
        self.assertIn("generic_modular_parity_proof", action_names)

    def test_formal_ir_value_problem(self):
        formal = compile_formal_ir(r"実数 $x,y$ が $x+y=5$ かつ $xy=6$ を満たすとき、$x^2+y^2$ を求めよ。")
        self.assertEqual(formal.status, "type_checked")
        self.assertIn("(declare x Real)", formal.sexpr)
        self.assertIn("(meta a Real)", formal.sexpr)
        self.assertIn("(= a (+ (^ x 2) (^ y 2)))", formal.sexpr)

    def test_formal_ir_all_solutions_problem(self):
        formal = compile_formal_ir(r"方程式 $x^2-5*x+6=0$ を満たす実数 $x$ をすべて求めよ。")
        self.assertEqual(formal.status, "type_checked")
        self.assertIn("(meta S (Set Real))", formal.sexpr)
        self.assertIn("(iff (member x S)", formal.sexpr)

    def test_formal_ir_existence_range_problem(self):
        formal = compile_formal_ir(r"実数 $x$ が $x^2-a*x+1=0$ を満たすような実数 $a$ の範囲を求めよ。")
        self.assertEqual(formal.status, "type_checked")
        self.assertIn("(meta S (Set Real))", formal.sexpr)
        self.assertIn("(exists ((x Real))", formal.sexpr)

    def test_formal_ir_does_not_evaluate_large_factorial(self):
        formal = compile_formal_ir(r"$2025!-1$は素数か。")
        self.assertIn("(factorial 2025)", formal.sexpr)

    def test_tex_input_scanner_splits_math_modes(self):
        text, spans = split_tex_text_math(r"価格は \$5。式は $x^2+1$ と \(y=\frac{1}{x+1}\)。")
        self.assertEqual(len(spans), 2)
        self.assertIn(r"\$5", text)
        self.assertIn("x**2+1", text)
        self.assertIn("y=((1)/(x+1))", text)

    def test_latex_frontend_uses_scanner_for_display_math(self):
        parsed = parse_latex_problem(r"求めよ \[ \frac{x^2-1}{x-1} \] ただし $x\ne1$.")
        self.assertIn("((x**2-1)/(x-1))", parsed.normalized_text)
        self.assertIn("x!=1", parsed.normalized_text)
        self.assertEqual(len(parsed.math_segments), 2)

    def test_latex_text_macro_style_problem_solves(self):
        problem = (
            r"$\text{実数 }x,y\text{ が }x+y=5\text{ かつ }xy=6"
            r"\text{ を満たすとき、}x^2+y^2\text{ を求めよ。}$"
        )
        parsed = parse_latex_problem(problem)
        self.assertIn("実数 x,y", parsed.normalized_text)
        self.assertIn("x**2+y**2", parsed.normalized_text)
        result = solve_request_payload({"problem": problem, "full_pipeline": True})
        self.assertEqual(result["answer"], "13")

    def test_equilateral_triangle_centroid_locus_area_compiles_to_constraints(self):
        problem = (
            r"$\text{曲線 }$y=x^3−2x"
            r"$\text{ 上の3点を頂点とする正三角形の重心の軌跡が囲む部分の面積を求めよ }$"
        )
        result = solve_request_payload({"problem": problem, "full_pipeline": True})
        self.assertTrue(result["ok"])
        self.assertEqual(result["data"]["parser"]["intent"], "latex_to_equilateral_triangle_centroid_locus_area")
        self.assertIsNone(result["answer"])
        self.assertEqual(result["data"]["math_search"]["answer"], None)
        self.assertNotIn("sympy.envelope", [call["name"] for call in result["data"]["tool_execution"]["tool_calls"]])
        tool_call = result["data"]["tool_execution"]["tool_calls"][0]
        self.assertEqual(tool_call["name"], "geometry.constraint_ir")
        self.assertEqual(tool_call["result"]["status"], "formalized")
        self.assertTrue(tool_call["result"]["no_memorized_answer"])
        self.assertIn("PointOnCurve", [constraint["type"] for constraint in tool_call["result"]["constraints"]])
        self.assertIn("Equilateral", [constraint["type"] for constraint in tool_call["result"]["constraints"]])
        self.assertEqual(tool_call["result"]["query"]["type"], "AreaOfBoundedLocus")
        self.assertEqual(result["data"]["formal_ir"]["metas"][0]["name"], "A")
        self.assertIn("geometry_constraint_compilation", [strategy["name"] for strategy in result["data"]["strategies"]])

    def test_equilateral_triangle_centroid_locus_coeff_change_uses_same_ir(self):
        problem = (
            r"$\text{曲線 }$y=x^3−3x"
            r"$\text{ 上の3点を頂点とする正三角形の重心の軌跡が囲む部分の面積を求めよ }$"
        )
        result = solve_request_payload({"problem": problem, "full_pipeline": True})
        self.assertTrue(result["ok"])
        self.assertIsNone(result["answer"])
        tool_call = result["data"]["tool_execution"]["tool_calls"][0]
        self.assertEqual(tool_call["name"], "geometry.constraint_ir")
        self.assertEqual(tool_call["result"]["status"], "formalized")
        self.assertEqual(tool_call["result"]["objects"][0]["equation"], "y = x**3-3*x")
        self.assertEqual(tool_call["result"]["query"]["type"], "AreaOfBoundedLocus")

    def test_web_solution_url_parser(self):
        url = "https://math.stackexchange.com/questions/1234567/example-title"
        self.assertEqual(extract_stackexchange_question_id(url), 1234567)

    def test_solution_step_parser_and_verifier(self):
        text = "Assume x is real. We have x^2 + 2*x + 1 = (x+1)^2. Therefore the expressions are equal."
        parsed = SolutionStepParser().parse_answer(text, source_url="memory://test", answer_id=1)
        self.assertTrue(parsed.steps)
        verified = StepVerifier(external_tools=False).verify_solution(parsed)
        self.assertGreaterEqual(verified.total_steps, 1)
        self.assertGreaterEqual(verified.verified_steps, 1)

    def test_query_builder_for_container_problem(self):
        text = r"平面上に一辺$\sqrt3$の正方形を固定する.一辺$\sqrt2+\sqrt6$の正三角形を, この正方形を含むように自由に動かすとき, 正三角形の通過領域の面積を求めよ."
        queries = QueryBuilder().build(text)
        self.assertIn("moving equilateral triangle contains square swept area", queries)

    def test_hybrid_retriever_offline(self):
        text = "曲線 y = t*x - t^2 の包絡線を求めよ。"
        result = HybridRetriever(live_search=False).retrieve(text, {"intent": "geometry_nl_to_dsl_envelope"})
        self.assertTrue(result["hits"])
        self.assertFalse(result["live_search"])

    def test_full_reasoning_pipeline_container_problem(self):
        text = r"平面上に一辺$\sqrt3$の正方形を固定する.一辺$\sqrt2+\sqrt6$の正三角形を, この正方形を含むように自由に動かすとき, 正三角形の通過領域の面積を求めよ."
        result = run_reasoning_pipeline(text)
        self.assertEqual(result.parser["intent"], "latex_to_container_square_in_equilateral_triangle_sweep")
        self.assertTrue(result.memory_retrieval["hits"])
        self.assertEqual(result.verification["status"], "verified")
        self.assertIn("Answer:", result.explanation)

    def test_web_app_rejects_empty_problem(self):
        result = solve_request_payload({"problem": ""})
        self.assertFalse(result["ok"])
        self.assertIn("問題文", result["error"])

    def test_web_app_replies_to_problem(self):
        text = r"平面上に一辺$\sqrt3$の正方形を固定する.一辺$\sqrt2+\sqrt6$の正三角形を, この正方形を含むように自由に動かすとき, 正三角形の通過領域の面積を求めよ."
        result = solve_request_payload({"problem": text, "full_pipeline": True})
        self.assertTrue(result["ok"])
        self.assertEqual(result["mode"], "full_pipeline")
        self.assertIn("Answer:", result["reply"])
        self.assertIn("data", result)

    def test_web_app_extracts_non_geometry_answers(self):
        algebra = solve_request_payload({"problem": "solve x^2 - 5*x + 6 = 0 for x", "full_pipeline": True})
        calculus = solve_request_payload({"problem": "derivative x^3 + 2*x with respect to x", "full_pipeline": True})
        convex = solve_request_payload(
            {
                "problem": "Minkowski sum [(0,0),(1,0),(1,1),(0,1)] + [(0,0),(2,0),(0,1)]",
                "full_pipeline": True,
            }
        )
        self.assertEqual(algebra["answer"], "['2', '3']")
        self.assertEqual(calculus["answer"], "3*x**2 + 2")
        self.assertIn("[3, 1]", convex["answer"])

    def test_polynomial_remainder_problem(self):
        ir = run_pipeline(r"$x^30$を$(x-1)^2$で割った余りを求めよ。")
        self.assertEqual(ir.intent, "latex_to_polynomial_remainder")
        self.assertEqual(ir.tool_calls[0].result["remainder"], "30*x - 29")
        result = solve_request_payload({"problem": r"$x^30$を$(x-1)^2$で割った余りを求めよ。", "full_pipeline": True})
        self.assertEqual(result["answer"], "30*x - 29")

    def test_japanese_polynomial_equation_pipeline(self):
        result = solve_request_payload({"problem": r"$x^3-6*x^2+11*x-6=0$ を解け。", "full_pipeline": True})
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "['1', '2', '3']")

    def test_number_theory_factorial_weeks_adapter(self):
        result = solve_request_payload(
            {
                "problem": r"$m$週間と$n!$秒が等しくなる非負整数の組($m,n$)をすべて求めよ.",
                "full_pipeline": True,
                "allow_specialized": True,
            }
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "n >= 10, m = n!/604800")
        self.assertEqual(result["data"]["tool_execution"]["tool_calls"][0]["name"], "number_theory.factorial_weeks")

    def test_coordinate_geometry_circle_overlap_limit_adapter(self):
        text = (
            r"半径$n$の2円の中心間距離が $n+\frac12,\sqrt{n(n+1)}$のときの共通部分の面積を "
            r"$S_n,T_n$ とする. $\lim_{n\to\infty}(S_n-T_n)$ を求めよ."
        )
        result = solve_request_payload({"problem": text, "full_pipeline": True, "allow_specialized": True})
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "-sqrt(3)/8")
        self.assertEqual(result["data"]["tool_execution"]["tool_calls"][0]["name"], "geometry.circle_overlap_limit")

    def test_probability_two_card_correlation_adapter(self):
        text = (
            r"1から$n$までの自然数が書かれたカードが1枚ずつあり，2枚を同時に引いたカードの値の"
            r"相加平均，相乗平均を $X_n,Y_n$ とする．また，$X_n,Y_n$ の相関係数を $\rho_n$ とする．"
            r"$\lim_{n\to\infty}\rho_n$ を求めよ．"
        )
        result = solve_request_payload({"problem": text, "full_pipeline": True, "allow_specialized": True})
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "8*sqrt(6)/(5*sqrt(17))")
        self.assertEqual(result["data"]["tool_execution"]["tool_calls"][0]["name"], "probability.two_card_correlation_limit")

    def test_probability_k_card_angle_adapter(self):
        text = (
            r"1から$n$までの自然数が書かれたカードが1枚ずつあり，$k(<n)$枚を同時に引き，"
            r"その相加平均，相乗平均を$X_{n,k},Y_{n,k}$とし，$X_{n,k}$と$Y_{n,k}$の相関係数を"
            r"$\cos\theta_{n,k}$とする. $\lim_{k\to\infty}\lim_{n\to\infty}\theta_{n,k}$ を求めよ."
        )
        result = solve_request_payload({"problem": text, "full_pipeline": True, "allow_specialized": True})
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "pi/6")
        self.assertEqual(result["data"]["tool_execution"]["tool_calls"][0]["name"], "probability.k_card_angle_limit")

    def test_inequality_counterexample_adapter(self):
        result = solve_request_payload(
            {"problem": "x>0 のとき x^2 < x を示せ.", "full_pipeline": True, "allow_specialized": True}
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["answer"], "{'x': 1}")
        self.assertEqual(result["data"]["tool_execution"]["tool_calls"][0]["name"], "inequality.counterexample_search")

    def test_container_geometry_detects_square_triangle_problem(self):
        text = r"平面上に一辺$\sqrt3$の正方形を固定する.一辺$\sqrt2+\sqrt6$の正三角形を, この正方形を含むように自由に動かすとき, 正三角形の通過領域の面積を求めよ."
        problem = detect_container_problem(text)
        self.assertIsNotNone(problem)
        self.assertEqual(problem.fixed_side, "sqrt(3)")
        self.assertEqual(problem.moving_side, "sqrt(2)+sqrt(6)")

    def test_container_geometry_solves_square_triangle_problem(self):
        text = r"平面上に一辺$\sqrt3$の正方形を固定する.一辺$\sqrt2+\sqrt6$の正三角形を, この正方形を含むように自由に動かすとき, 正三角形の通過領域の面積を求めよ."
        problem = detect_container_problem(text)
        result = solve_container_problem(problem)
        self.assertEqual(result["status"], "solved")
        self.assertIn("2*pi*(2*sqrt(3) + 5)", result["answer_exact"])

    def test_math_os_solves_container_problem(self):
        text = r"平面上に一辺$\sqrt3$の正方形を固定する.一辺$\sqrt2+\sqrt6$の正三角形を, この正方形を含むように自由に動かすとき, 正三角形の通過領域の面積を求めよ."
        ir = run_pipeline(text)
        self.assertEqual(ir.intent, "latex_to_container_square_in_equilateral_triangle_sweep")
        self.assertEqual(ir.tool_calls[0].result["status"], "solved")

    def test_latex_frontend_normalizes_region_problem(self):
        latex = r"""
        \begin{problem}
        $t\in\mathbb{R}$ とする。曲線 \( y = tx - t^2 \) の通過領域を求めよ。
        \end{problem}
        """
        parsed = parse_latex_problem(latex)
        self.assertIn("t in R", parsed.normalized_text)
        self.assertIn("y = t*x - t**2", parsed.normalized_text)

    def test_math_os_runs_latex_region_problem(self):
        latex = r"\begin{problem}$t\in\mathbb{R}$ とする。曲線 \( y = tx - t^2 \) の通過領域を求めよ。\end{problem}"
        ir = run_pipeline(latex)
        self.assertEqual(ir.intent, "latex_to_geometry_nl_to_dsl_region")
        self.assertEqual(ir.tool_calls[0].result["result"]["closed_form"]["inequality"], "y <= x**2/4")

    def test_tool_registry_reports_sympy(self):
        status = ToolRegistry().status()
        self.assertTrue(status["sympy"]["available"])
        self.assertIn("available", status["wolfram"])
        self.assertIn("available", status["z3"])
        self.assertIn("available", status["shapely"])
        self.assertIn("available", status["lean"])

    def test_wolfram_code_for_region(self):
        problem = parse_geometry_dsl("task region; family y = t*x - t^2; param t in R")
        code = wolfram_code_for_geometry(problem)
        self.assertIn("Reduce[Exists[t", code)
        self.assertIn("y == t*x - t^2", code)

    def test_geometry_nl_region_conversion(self):
        conversion = convert_geometry_nl("tを実数として、曲線 y = t*x - t^2 の通過領域を求めよ。")
        self.assertIsNotNone(conversion)
        self.assertEqual(conversion.dsl, "task region; family y = t*x-t**2; param t in R")

    def test_geometry_nl_envelope_conversion(self):
        conversion = convert_geometry_nl("曲線 y = t*x - t^2 の包絡線を求めよ。")
        self.assertIsNotNone(conversion)
        self.assertEqual(conversion.task, "envelope")
        self.assertEqual(conversion.equations["y"], "t*x-t**2")

    def test_geometry_nl_locus_coordinate_pair(self):
        conversion = convert_geometry_nl("(x,y)=(t+1,2t) で表される点の軌跡を求めよ。")
        self.assertIsNotNone(conversion)
        self.assertEqual(conversion.dsl, "task locus; x = t+1; y = 2*t; param t in R")

    def test_math_os_runs_natural_language_region(self):
        ir = run_pipeline("tを実数として、曲線 y = t*x - t^2 の通過領域を求めよ。")
        self.assertEqual(ir.intent, "geometry_nl_to_dsl_region")
        self.assertEqual(ir.tool_calls[0].result["result"]["closed_form"]["inequality"], "y <= x**2/4")
        self.assertEqual(ir.tool_calls[0].result["tool_results"][0]["tool"], "sympy")

    def test_geometry_dsl_envelope_execution(self):
        result = run_geometry_dsl("task envelope; family y = t*x - t^2; param t")
        self.assertEqual(result["problem"]["task"], "envelope")
        self.assertEqual(result["result"]["envelope_relation"], "-x**2 + 4*y")

    def test_geometry_dsl_region_unbounded_quadratic(self):
        result = run_geometry_dsl("task region; family y = t*x - t^2; param t in R")
        closed_form = result["result"]["closed_form"]
        self.assertEqual(closed_form["type"], "quadratic_range")
        self.assertEqual(closed_form["inequality"], "y <= x**2/4")

    def test_geometry_dsl_locus_execution(self):
        result = run_geometry_dsl("task locus; x = t + 1; y = 2*t; param t")
        self.assertEqual(result["result"]["locus_relation"], "2*x - y - 2")

    def test_geometry_dsl_parser_interval(self):
        problem = parse_geometry_dsl("task region; family y = t*x - t^2; param t in [0,2]")
        self.assertEqual(problem.domain.kind, "interval")
        self.assertEqual(problem.domain.lower, "0")
        self.assertEqual(problem.domain.upper, "2")

    def test_math_os_detects_geometry_dsl(self):
        ir = run_pipeline("task region; family y = t*x - t^2; param t in R")
        self.assertEqual(ir.intent, "geometry_dsl_region")
        self.assertEqual(ir.tool_calls[0].result["result"]["closed_form"]["inequality"], "y <= x**2/4")

    def test_envelope_execution(self):
        ir = run_pipeline("包絡線 y = t*x - t^2 を求めて。parameter t")
        self.assertEqual(ir.route, "geometry_symbolic")
        result = ir.tool_calls[0].result
        self.assertIsNotNone(result)
        if "result" in result:
            result = result["result"]
        self.assertEqual(result["envelope_relation"], "-x**2 + 4*y")

    def test_minkowski_sum_execution(self):
        ir = run_pipeline(
            "Minkowski sum [(0,0),(1,0),(1,1),(0,1)] + [(0,0),(2,0),(0,1)]"
        )
        self.assertEqual(ir.route, "convex_geometry")
        self.assertEqual(ir.tool_calls[0].result["vertices"], [[0, 0], [3, 0], [3, 1], [1, 2], [0, 2]])

    def test_formal_proof_is_planned(self):
        ir = run_pipeline("Leanで n + 0 = n を証明したい")
        self.assertEqual(ir.route, "formal_proof")
        self.assertFalse(ir.tool_calls[0].executable)
        self.assertIn("import Mathlib", ir.givens["lean_stub"])

    def test_router_can_train_from_seed_examples(self):
        router = TinyRouter()
        decision = router.route("diagram parser")
        self.assertIn(decision.label, set(router.route("diagram parser").scores))

    def test_compiler_without_execution(self):
        compiler = ProblemCompiler()
        ir = compiler.compile("solve x^2 - 5*x + 6 = 0 for x")
        ToolExecutor().execute(ir)
        self.assertEqual(ir.tool_calls[0].result["solutions"], ["2", "3"])

    def test_symbolic_query_ir_preserves_query_operator(self):
        cases = [
            ("Expand $(3x^2+2x)(x^2-5)$.", "expand", "3*x**4 + 2*x**3 - 15*x**2 - 10*x"),
            ("Factor $5x^2-45$.", "factor", "5*(x - 3)*(x + 3)"),
            ("If $(3x+1)(x-2)=7$, find the sum of the possible values of $x$.", "root_sum", "5/3"),
            ("What value of $x$ gives the minimum value of $2x^2-20x+1$?", "argmin", "5"),
            ("Given that $-6$ is a solution to $x^2+bx-42=0$, what is the value of $b$?", "solve", "-1"),
            ("If $r$ and $s$ are the roots of $3x^2-7x+2=0$, find $(r-2)(s-2)$.", "symmetric_root_expression", "0"),
        ]
        for problem, operator, expected in cases:
            with self.subTest(operator=operator):
                ir = run_pipeline(problem)
                self.assertEqual(ir.intent, f"symbolic_query_{operator}")
                self.assertEqual(ir.tool_calls[0].result["query_operator"], operator)
                self.assertEqual(ir.tool_calls[0].result["answer_exact"], expected)

    def test_symbolic_query_ir_lifts_to_typed_semantic_graph(self):
        result = solve_request_payload(
            {
                "problem": "For what values of $x$ is $x^2-5x-4 \\le 10$? Express the answer in interval notation.",
                "full_pipeline": True,
            }
        )
        self.assertEqual(result["answer"], "Interval(-2, 7)")
        graph = result["data"]["semantic_graph"]
        self.assertTrue(any(item["name"] == "solve_inequality" for item in graph["morphisms"]))
        self.assertTrue(any(item["kind"] == "solve_inequality" and item["sort"] == "Set" for item in graph["queries"]))

    def test_symbolic_query_expands_chained_inequality_as_constraint_intersection(self):
        result = solve_request_payload(
            {
                "problem": "For what real values of $u$ is $-5<u^4+5u^2<24$ satisfied? Express the answer in interval notation.",
                "full_pipeline": True,
            }
        )
        self.assertEqual(result["answer"], "Interval.open(-sqrt(3), sqrt(3))")
        symbolic_ir = result["data"]["parser"]["givens"]["symbolic_query"]
        self.assertEqual(symbolic_ir["constraints"], ["-5<u**4+5*u**2", "u**4+5*u**2<24"])

    def test_generic_equation_solver_cannot_answer_an_unreached_aggregate_query(self):
        result = solve_request_payload(
            {
                "problem": "The roots of $z^6+z^4+z^2+1=0$ are vertices of a convex polygon. Find the sum of the squares of its side lengths.",
                "full_pipeline": True,
            }
        )
        self.assertIsNone(result["answer"])
        operations = result["data"]["structural_ir"]["operations"]
        self.assertTrue(any(item["kind"] == "aggregate" for item in operations))


if __name__ == "__main__":
    unittest.main()
