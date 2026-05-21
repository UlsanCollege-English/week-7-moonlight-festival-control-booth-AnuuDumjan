"""
Week 7: Moonlight Festival Control Booth

Use Python's heapq module to solve priority queue problems.
"""

from __future__ import annotations

import heapq


def order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles ordered from most urgent
    to least urgent.
    """

    heap = alerts[:]
    heapq.heapify(heap)

    result = []

    while heap:
        priority, title = heapq.heappop(heap)
        result.append(title)

    return result


def order_festival_alerts_stable(
    alerts: list[tuple[int, str]]
) -> list[str]:
    """
    Return alert titles ordered by priority.

    Alerts with the same priority keep their
    original input order.
    """

    heap = []

    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    result = []

    while heap:
        priority, index, title = heapq.heappop(heap)
        result.append(title)

    return result


def top_k_festival_alerts(
    alerts: list[tuple[int, str]],
    k: int
) -> list[str]:
    """
    Return the k most urgent alert titles.
    """

    if k <= 0:
        return []

    heap = []

    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    result = []

    for _ in range(min(k, len(heap))):
        priority, index, title = heapq.heappop(heap)
        result.append(title)

    return result


def peek_next_festival_alert(
    alerts: list[tuple[int, str]]
) -> str | None:
    """
    Return the next alert without changing
    the original input.
    """

    if not alerts:
        return None

    heap = [
        (priority, index, title)
        for index, (priority, title) in enumerate(alerts)
    ]

    heapq.heapify(heap)

    return heap[0][2]