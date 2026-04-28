"""
Week 7: Moonlight Festival Control Booth

Use Python's heapq module to solve priority queue problems.
"""

from __future__ import annotations

import heapq


def order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]:
    heap = alerts[:]
    heapq.heapify(heap)

    result = []

    while heap:
        priority, title = heapq.heappop(heap)
        result.append(title)

    return result


def order_festival_alerts_stable(alerts: list[tuple[int, str]]) -> list[str]:
    heap = []

    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    result = []

    while heap:
        priority, index, title = heapq.heappop(heap)
        result.append(title)

    return result


def top_k_festival_alerts(alerts: list[tuple[int, str]], k: int) -> list[str]:
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


def peek_next_festival_alert(alerts: list[tuple[int, str]]) -> str | None:
    if not alerts:
        return None

    heap = []

    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    priority, index, title = heapq.heappop(heap)
    return title