from lark import Lark
from typing import Tuple, Any


class Environment(object):
    def __init__(self, parent_env):
        self._parent_env = parent_env
        self._env = dict()

    def get(self, key, default=None):
        value = self._env.get(key, None)
        if value is None and self._parent_env:
            value = self._parent_env.get(key)
        if value is not None:
            return value
        return default

    def set(self, key, value):
        self._env[key] = value

    def __str__(self):
        return "{}".format(self._env)


class Visitor(object):
    def __default__(self, tree, env):
        raise

    def program(self, tree, env):
        for sub_tree in tree.children:
            r, f = self.visit(sub_tree, env)
            print("{}".format(r))
            if f:
                return r

    def return_state(self, tree, env) -> Tuple[Any, bool]:
        child = tree.children[0]
        value, _ = self.visit(child, env)
        print("return_state: {}".format(value))
        return value, True

    def escaped_value(self, tree, env) -> Tuple[Any, bool]:
        value = tree.children[0].value
        return value[1:len(value)-1], False

    def contains_expression(self, tree, env) -> Tuple[Any, bool]:
        value1, _ = self.visit(tree.children[0], env)
        result = False
        for i in range(1, len(tree.children)):
            value2, _ = self.visit(tree.children[i], env)
            result |= value2 in value1
            if result:
                break

        return result, False

    def or_expression(self, tree, env) -> Tuple[Any, bool]:
        result = False
        for i in range(0, len(tree.children)):
            key, _ = self.visit(tree.children[i], env)
            value2 = env.get(key)
            print("value2: {}".format(value2))
            result |= bool(value2)
            if result:
                break

        return result, False

    def not_expression(self, tree, env) -> Tuple[Any, bool]:
        print(tree)
        value, _ = self.visit(tree.children[0], env)
        return not value, False

    def set_state(self, tree, env) -> Tuple[Any, bool]:
        key, _ = self.visit(tree.children[0], env)
        value, _ = self.visit(tree.children[1], env)
        env.set(key, value)
        return None, False

    def if_state(self, tree, env) -> Tuple[Any, bool]:
        child = tree.children[0]
        if child.data == 'symbol':
            key, _ = self.visit(child, env)
            flag = env.get(key)
        else:
            flag, _ = self.visit(child, env)

        print("if_state: {}".format(flag))
        if flag:
            return self.visit(tree.children[1], env)
        else:
            return None, False

    def if_else_state(self, tree, env) -> Tuple[Any, bool]:
        child = tree.children[0]
        if child.data == 'symbol':
            key, _ = self.visit(child, env)
            flag = env.get(key)
        else:
            flag, _ = self.visit(child, env)

        print("if_else_state: {}".format(flag))
        if flag:
            return self.visit(tree.children[1], env)
        else:
            return self.visit(tree.children[2], env)

    def symbol(self, tree, env) -> Tuple[Any, bool]:
        return tree.children[0].value, False

    def reserved_symbol(self, tree, env) -> Tuple[Any, bool]:
        key, _ = self.visit(tree.children[0], env)
        return env.get(key), False

    def visit(self, tree, env) -> Tuple[Any, bool]:
        f = getattr(self, tree.data, self.__default__)
        return f(tree, env)


with open('program.txt', 'r') as reader:
    program = reader.read()

with open('grammar.txt', 'r') as reader:
    grammar = reader.read()


def execute(message: str):
    parser = Lark(grammar, start='program', parser='lalr')

    # プログラムを字句解析＆構文解析
    tree = parser.parse(program)

    print(tree)

    global_env = Environment(None)
    global_env.set("message", message)
    _visitor = Visitor()
    result = _visitor.visit(tree, global_env)

    print("result: {}".format(result))
    return result
