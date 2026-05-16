# 02 — `statistics` Module

## Import

```python
import statistics
```

No installation needed — part of Python's standard library.

## Key functions

| Function | What it returns | Example |
|----------|----------------|---------|
| `statistics.mean(data)` | Arithmetic average | `mean([100, 90])` → `95` |
| `statistics.median(data)` | Middle value | `median([1,2,3,4,5])` → `3` |
| `statistics.mode(data)` | Most frequent value | `mode(["A","A","B"])` → `"A"` |
| `statistics.stdev(data)` | Standard deviation | `stdev([2,4,4,4,5,5,7,9])` → `2.0` |

## Try it

```bash
python3 statistics_demo.py 80 90 100
# → Average: 90.0
```
