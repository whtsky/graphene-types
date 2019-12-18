from ..argument import Argument as Argument
from ..enum import Enum as Enum
from ..field import Field as Field
from ..inputfield import InputField as InputField
from ..inputobjecttype import InputObjectType as InputObjectType
from ..interface import Interface as Interface
from ..objecttype import ObjectType as ObjectType
from ..scalars import Boolean as Boolean, Int as Int, String as String
from ..schema import Schema as Schema
from ..structures import List as List, NonNull as NonNull
from ..union import Union as Union
from typing import Any

class Image(ObjectType):
    url: Any = ...
    width: Any = ...
    height: Any = ...

class Author(ObjectType):
    id: Any = ...
    name: Any = ...
    pic: Any = ...
    recent_article: Any = ...

class Article(ObjectType):
    id: Any = ...
    is_published: Any = ...
    author: Any = ...
    title: Any = ...
    body: Any = ...

class Query(ObjectType):
    article: Any = ...
    feed: Any = ...

class Mutation(ObjectType):
    write_article: Any = ...

class Subscription(ObjectType):
    article_subscribe: Any = ...

class MyObjectType(ObjectType): ...
class MyInterface(Interface): ...

class MyUnion(Union):
    class Meta:
        types: Any = ...

class MyEnum(Enum):
    foo: str = ...

class MyInputObjectType(InputObjectType): ...

def test_defines_a_query_only_schema() -> None: ...
def test_defines_a_mutation_schema() -> None: ...
def test_defines_a_subscription_schema() -> None: ...
def test_includes_nested_input_objects_in_the_map() -> None: ...
def test_includes_interfaces_thunk_subtypes_in_the_type_map() -> Any: ...
def test_includes_types_in_union() -> None: ...
def test_maps_enum() -> None: ...
def test_includes_interfaces_subtypes_in_the_type_map() -> None: ...
def test_stringifies_simple_types() -> None: ...
def test_does_not_mutate_passed_field_definitions() -> None: ...