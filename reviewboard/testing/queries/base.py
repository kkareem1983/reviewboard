"""Base patterns and support for defining expected queries for unit tests.

Version Added:
    5.0.7
"""

from __future__ import annotations

from typing import Dict, Set, TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    from django.db.models import Q

    from djblets.db.query_comparator import ExpectedQueries


class ExpectedQResult(TypedDict):
    """An expected Q-expression result from a utility function.

    This should be used by unit test utility functions that build expected Q
    expressions in order to provide consistent results with typing.

    Version Added:
        5.0.7
    """

    #: The expected Q expression.
    q: Q

    #: The set of tables involved in the Q expression.
    tables: Set[str]

    #: The types of any joined tables.
    join_types: NotRequired[Dict[str, str]]

    #: Any queries that should be expected before a query using this Q.
    prep_equeries: NotRequired[ExpectedQueries]
