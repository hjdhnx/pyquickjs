#ifndef MODULE_LIBC_H
#define MODULE_LIBC_H

#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include "upstream-quickjs/cutils.h"
#include "upstream-quickjs/quickjs.h"

#ifdef __cplusplus
extern "C" {
#endif

const char *py_call_function(const char *module_name);

int py_module_set_import_meta(JSContext *ctx, JSValueConst func_val,
                              JS_BOOL use_realpath, JS_BOOL is_main);
JSModuleDef *py_module_loader(JSContext *ctx,
                              const char *module_name, void *opaque);

#ifdef __cplusplus
}
#endif

#endif
