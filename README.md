# dockerfile-tool
Coding Challenge.

P.S.: The bonus part, running as Kubernetes job, is a Work In Progress (Missing binding the volume to output the json and some minor improvements).

For now, it can be executed with:
* `python3 dockerfile-list-tool.py $REPOSITORY_LIST_URL`

* `docker run --env REPOSITORY_LIST_URL="https://gist.githubusercontent.com/jmelis/c60e61a893248244dc4fa12b946585c4/raw/25d39f67f2405330a6314cad64fac423a171162c/sources.txt" avelarana/rhchallenge:1.0`
(missing the volume bind for the output json, in progress).

The generated json is named `imageslist.json`.

Code decisions
---

Since it is a small python script, it was preferred to implement not object oriented, for Performance.

There are more improvements that can be done, but here is a first version.
