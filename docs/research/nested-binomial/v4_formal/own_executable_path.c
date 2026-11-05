#define _GNU_SOURCE
#include <dlfcn.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>

/* This executor exposes /proc/self/exe but not /proc/<own-pid>/exe.
   Preserve readlink semantics except for that equivalent own-process path.
   This does not change Lean's mathematical kernel or library sources. */
ssize_t readlink(const char *path, char *buf, size_t size) {
    static ssize_t (*original)(const char *, char *, size_t) = NULL;
    if (!original) original = dlsym(RTLD_NEXT, "readlink");
    ssize_t result = original(path, buf, size);
    if (result < 0 && errno == ENOENT) {
        char own[128];
        snprintf(own, sizeof own, "/proc/%ld/exe", (long)getpid());
        if (strcmp(path, own) == 0) return original("/proc/self/exe", buf, size);
    }
    return result;
}
