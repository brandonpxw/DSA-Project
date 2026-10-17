# Data Structures & Algorithms Project

A command-line program that manages activity package bookings with classic sorting and searching
algorithms, each written by hand.

**Nanyang Polytechnic · Year 2 · 2022**

## What it does

| Menu option | Algorithm |
|---|---|
| Sort by customer name | Bubble sort |
| Sort by package name | Selection sort |
| Sort by package cost | Insertion sort |
| Find a customer and update their booking | Linear (sequential) search |
| Find a package and update its booking | Binary search |
| Search by package cost | Quicksort (bonus) |

It can also list every booking, or only those within a cost range.

## Running it

Needs Python 3, with no extra packages.

```
python codes.py
```

Then pick an option from the menu.

## How quicksort works

Quicksort picks one element as the pivot, then splits the list into the elements smaller than
the pivot and those greater than or equal to it. It sorts each part the same way until every
part has one element. It sorts in place, so it needs little extra memory, and on average it
takes O(n log n) time, which makes it one of the fastest general-purpose sorts.

## What I learned

This was my first time learning sorting and searching algorithms. It showed me how everyday
features like a search bar or "sort by price" actually work underneath.
