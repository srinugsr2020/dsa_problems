"""Normalize an absolute Unix path lexically, without touching the filesystem."""

import posixpath


def simplify_by_splitting(path):
    if not path.startswith("/"):
        raise ValueError("expected an absolute path")
    stack = []
    for part in path.split("/"):
        if part == "..":
            if stack:
                stack.pop()
        elif part not in ("", "."):
            stack.append(part)
    return "/" + "/".join(stack)


def simplify_with_posixpath(path):
    if not path.startswith("/"):
        raise ValueError("expected an absolute path")
    return posixpath.normpath("/" + path.lstrip("/"))


def simplify_by_scanning_backward(path):
    if not path.startswith("/"):
        raise ValueError("expected an absolute path")
    kept = []
    parents = 0
    end = len(path)
    while end:
        start = path.rfind("/", 0, end) + 1
        size = end - start
        if size == 2 and path[start] == "." and path[start + 1] == ".":
            parents += 1
        elif size and not (size == 1 and path[start] == "."):
            if parents:
                parents -= 1
            else:
                kept.append(path[start:end])
        end = start - 1
    return "/" + "/".join(reversed(kept))


if __name__ == "__main__":
    for solve in (simplify_by_splitting, simplify_with_posixpath, simplify_by_scanning_backward):
        assert solve("//srv//./share/") == "/srv/share"
        assert solve("/../a/./b/../../c//") == "/c"
        assert solve("/.../.hidden/a../.") == "/.../.hidden/a.."
        assert solve("/a/../../b") == "/b"
        assert solve("/a/../..////") == "/"
        assert solve("////") == "/"
        assert solve("/" + "large" * 2048 + "/../kept") == "/kept"
        for path in ("", "a/../b"):
            try:
                solve(path)
            except ValueError:
                pass
            else:
                raise AssertionError(f"Accepted a non-absolute path: {path!r}")
