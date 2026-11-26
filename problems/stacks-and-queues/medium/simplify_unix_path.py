"""=============================================================================
MEDIUM (Stack): Simplify Unix Path
=============================================================================

Given an absolute Unix-style path, simplify it.

Rules:
    - "/." means current directory -> ignore
    - "/.." means parent directory -> pop one directory if possible
    - Multiple slashes are treated as a single slash
    - The result must:
        - start with '/'
        - not end with '/' (unless the result is '/')

Examples:
    path = "/home/"            -> "/home"
    path = "/../"              -> "/"
    path = "/home//foo/"       -> "/home/foo"
    path = "/a/./b/../../c/"   -> "/c"

Constraints (assume):
    - 0 <= len(path) <= 200_000

Target:
    - Time:  O(n)
    - Space: O(n)

Hints:
    - Split by '/'
    - Use a stack for directory names

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `simplify_path(path: str) -> str`.
"""

from __future__ import annotations


def simplify_path(path: str) -> str:
    """Return the simplified canonical path."""

    # TODO: Implement.
    stack = []
    for part in path.split('/'):
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)


def _run_samples() -> None:
    assert simplify_path("/home/") == "/home"
    assert simplify_path("/../") == "/"
    assert simplify_path("/home//foo/") == "/home/foo"
    assert simplify_path("/a/./b/../../c/") == "/c"

    # Edge cases
    assert simplify_path("/") == "/"
    assert simplify_path("////") == "/"
    assert simplify_path("/a/../../b/../c//.//") == "/c"


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
