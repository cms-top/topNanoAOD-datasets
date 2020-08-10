from __future__ import print_function
"""
Check that no duplicates are present in the YAML files.

Use with "python -i loadYAML_checkDuplicates.py"
or "ipython -i loadYAML_checkDuplicates.py" to quickly get the
parsed YAML files (in the ``datasets`` variable).
"""
import yaml

# recipe based on https://stackoverflow.com/a/48460700/11079521
class YAMLDuplicateCheckLoader(yaml.SafeLoader):
    pass

def map_constructor_check_duplicates(loader, node, deep=False):
    mapping = dict()
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        value = loader.construct_object(value_node, deep=deep)
        if key in mapping:
            raise RuntimeError("{0} line {1:d} column {2:d}: key {3!s} is already present in mapping starting on line {4:d} column {5:d}".format(
                key_node.start_mark.name, key_node.start_mark.line+1, key_node.start_mark.column,
                key, node.start_mark.line+1, node.start_mark.column))
        mapping[key] = value
    return mapping

YAMLDuplicateCheckLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, map_constructor_check_duplicates)

if __name__ == "__main__":
    ## list YAML files and check them for duplicates
    import os, os.path
    from fnmatch import fnmatch
    datasets = dict()
    here = os.path.abspath(os.path.dirname(__file__))
    for fn in os.listdir(here):
        if fnmatch(fn, "*.yml") and fn != ".travis.yml":
            with open(os.path.join(here, fn)) as yF:
                datasets[fn[:-4]] = yaml.load(yF, YAMLDuplicateCheckLoader)
