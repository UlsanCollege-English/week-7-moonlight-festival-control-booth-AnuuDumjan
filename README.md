[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-HC-VniT)
# Week 7 Homework: Moonlight Festival Control Booth

## Summary

This homework uses Python’s heapq module to manage festival alerts by priority.
Each alert has a priority number and a title, where smaller numbers mean more urgent alerts.
The program sorts alerts, keeps stable order for ties, finds the top k urgent alerts, and checks the next alert without changing the original list.

---

## Approach

### order_festival_alerts

I copied the original alerts list and turned it into a heap using heapq.heapify().
Each heap item looked like (priority, title).
Since Python compares tuples from left to right, the smallest priority comes first.
I used heappop() again and again to remove the smallest item and added only the title to the result list.

### order_festival_alerts_stable

To handle ties, I added the original index of each alert.
Each heap item looked like (priority, index, title).
If two alerts had the same priority, Python compared the index next, so the earlier input stayed first.
Input order mattered because alerts with the same urgency should be handled fairly.

### top_k_festival_alerts

I first checked if k <= 0, and returned an empty list.
Then I made a heap and used heappop() only k times.
This allowed me to collect only the most urgent alerts instead of all alerts.
If k was larger than the number of alerts, I used min(k, len(heap)) so it would not cause an error.

### peek_next_festival_alert

I made a copy of the alerts list so the original data would not change.
Then I turned the copy into a heap and used heappop() once to see the next alert.
This returned the most urgent title without permanently changing the original input.

---

## Complexity

### order_festival_alerts

Time: O(n log n)
Space: O(n)
Why: Creating the heap takes O(n), and removing all n items takes O(log n) each.

### order_festival_alerts_stable

Time: O(n log n)
Space: O(n)
Why: Each item is pushed into the heap and popped once. Both operations are O(log n).

### top_k_festival_alerts

Time: O(n + k log n)
Space: O(n)
Why: Heap creation is O(n), and only k items are removed using heappop().

### peek_next_festival_alert

Time: O(n)
Space: O(n)
Why: Copying and heapifying the list takes O(n), and one pop is very small after that.

---

## Edge-case checklist

### order_festival_alerts

[x] empty input
[x] one alert
[x] multiple different priorities

### order_festival_alerts_stable

[x] same-priority tie
[x] all same priority
[x] empty input

### top_k_festival_alerts

[x] k = 0
[x] k > len(alerts)
[x] duplicate priorities
[x] empty input

### peek_next_festival_alert

[x] empty input
[x] normal case

---

## Test notes

- I tested with alerts having different priorities to check correct ordering.
- I tested same-priority alerts to confirm stable order was preserved.
- I tested empty lists and large k values to make sure no errors happened.

---

## Assistance & Sources

### AI used?

[x] Yes

If yes, what did it help with?

It helped me understand how heapq works and how to write cleaner Python code using heaps.

### Other sources

- Python official documentation for heapq
- Class notes and examples from lecture

---

## Reflection

What was hardest?

The hardest part was understanding how stable ordering works when two priorities are the same.

What do you understand better now?

I understand better how heaps work, how heapq organizes data, and why tuples with indexes help solve tie-breaking problems.