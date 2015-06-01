#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Git commit-msg hook for sniprd.

FROM: http://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
The commit-msg hook takes one parameter, which again is the path to
a temporary file that contains the commit message written by the
developer. If this script exits non-zero, Git aborts the commit
process, so you can use it to validate your project state or commit
message before allowing a commit to go through.
"""

from status_report.utils import log, LOG_DEBUG

# Turn on DEBUG so we can get a full log on each commit
log.setLevel(LOG_DEBUG)

import sys


def main():
    py, msg_pth = sys.argv  # noqa
    msg_summary = open(msg_pth).readlines()[0]
    k = len(msg_summary)
    x = k - 50 - 1
    if len(msg_summary) > 50:
        log.error("Commit Message Check: FAIL")
        log.error("Your commit message:")
        log.error("\n{0}{1}{2}".format(msg_summary, '^' * 50, 'X' * x))
        log.error("""
<<<<| Commit msg summary must be <= 50 chars >>>>|
--------------------------------------------------
This is my commit message summary; Max length >>>|

After a line break (\\n) , the full description of
the commit can be included though. No Problem.""")
        sys.exit(1)
    else:
        log.warn("Commit Message Check: PASS")

if __name__ == '__main__':
    main()
    sys.exit(0)

sys.exit(1)
