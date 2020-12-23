
from buildbot.test.util import changesource
from buildbot.test.fake import httpclientservice as fakehttpclientservice
from buildbot.test.util.misc import TestReactorMixin

from twisted.trial import unittest
from twisted.internet import defer
from buildbot.plugins import *

import json

apiRepoList = """
[
  {
    "url": "https://api.github.com/repos/buildbot/buildbot/releases/27532254",
    "assets_url": "https://api.github.com/repos/buildbot/buildbot/releases/27532254/assets",
    "upload_url": "https://uploads.github.com/repos/buildbot/buildbot/releases/27532254/assets{?name,label}",
    "html_url": "https://github.com/buildbot/buildbot/releases/tag/v2.8.2",
    "id": 27532254,
    "node_id": "MDc6UmVsZWFzZTI3NTMyMjU0",
    "tag_name": "v2.8.2",
    "target_commitish": "master",
    "name": "v2.8.2",
    "draft": false,
    "author": {
      "login": "p12tic",
      "id": 1056711,
      "node_id": "MDQ6VXNlcjEwNTY3MTE=",
      "avatar_url": "https://avatars0.githubusercontent.com/u/1056711?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/p12tic",
      "html_url": "https://github.com/p12tic",
      "followers_url": "https://api.github.com/users/p12tic/followers",
      "following_url": "https://api.github.com/users/p12tic/following{/other_user}",
      "gists_url": "https://api.github.com/users/p12tic/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/p12tic/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/p12tic/subscriptions",
      "organizations_url": "https://api.github.com/users/p12tic/orgs",
      "repos_url": "https://api.github.com/users/p12tic/repos",
      "events_url": "https://api.github.com/users/p12tic/events{/privacy}",
      "received_events_url": "https://api.github.com/users/p12tic/received_events",
      "type": "User",
      "site_admin": false
    },
    "prerelease": false,
    "created_at": "2020-06-14T14:24:15Z",
    "published_at": "2020-06-14T14:32:01Z",
    "assets": [],
    "tarball_url": "https://api.github.com/repos/buildbot/buildbot/tarball/v2.8.2",
    "zipball_url": "https://api.github.com/repos/buildbot/buildbot/zipball/v2.8.2",
    "body": " - Fix crash in Buildbot Windows service startup code (#5344)\\r\\n"
  },
  {
    "url": "https://api.github.com/repos/buildbot/buildbot/releases/27532254",
    "assets_url": "https://api.github.com/repos/buildbot/buildbot/releases/27532254/assets",
    "upload_url": "https://uploads.github.com/repos/buildbot/buildbot/releases/27532254/assets{?name,label}",
    "html_url": "https://github.com/buildbot/buildbot/releases/tag/v2.8.2",
    "id": 27532254,
    "node_id": "MDc6UmVsZWFzZTI3NTMyMjU0",
    "tag_name": "v2.8.2",
    "target_commitish": "master",
    "name": "v2.8.2",
    "draft": false,
    "author": {
      "login": "p12tic",
      "id": 1056711,
      "node_id": "MDQ6VXNlcjEwNTY3MTE=",
      "avatar_url": "https://avatars0.githubusercontent.com/u/1056711?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/p12tic",
      "html_url": "https://github.com/p12tic",
      "followers_url": "https://api.github.com/users/p12tic/followers",
      "following_url": "https://api.github.com/users/p12tic/following{/other_user}",
      "gists_url": "https://api.github.com/users/p12tic/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/p12tic/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/p12tic/subscriptions",
      "organizations_url": "https://api.github.com/users/p12tic/orgs",
      "repos_url": "https://api.github.com/users/p12tic/repos",
      "events_url": "https://api.github.com/users/p12tic/events{/privacy}",
      "received_events_url": "https://api.github.com/users/p12tic/received_events",
      "type": "User",
      "site_admin": false
    },
    "prerelease": false,
    "created_at": "2020-06-14T14:24:15Z",
    "published_at": "2020-06-14T14:32:01Z",
    "assets": [],
    "tarball_url": "https://api.github.com/repos/buildbot/buildbot/tarball/v2.8.2",
    "zipball_url": "https://api.github.com/repos/buildbot/buildbot/zipball/v2.8.2",
    "body": " - Fix crash in Buildbot Windows service startup code (#5344)\\r\\n"
  },
  {
    "url": "https://api.github.com/repos/buildbot/buildbot/releases/27292648",
    "assets_url": "https://api.github.com/repos/buildbot/buildbot/releases/27292648/assets",
    "upload_url": "https://uploads.github.com/repos/buildbot/buildbot/releases/27292648/assets{?name,label}",
    "html_url": "https://github.com/buildbot/buildbot/releases/tag/v2.8.1",
    "id": 27292648,
    "node_id": "MDc6UmVsZWFzZTI3MjkyNjQ4",
    "tag_name": "v2.8.1",
    "target_commitish": "master",
    "name": "v2.8.1",
    "draft": false,
    "author": {
      "login": "p12tic",
      "id": 1056711,
      "node_id": "MDQ6VXNlcjEwNTY3MTE=",
      "avatar_url": "https://avatars0.githubusercontent.com/u/1056711?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/p12tic",
      "html_url": "https://github.com/p12tic",
      "followers_url": "https://api.github.com/users/p12tic/followers",
      "following_url": "https://api.github.com/users/p12tic/following{/other_user}",
      "gists_url": "https://api.github.com/users/p12tic/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/p12tic/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/p12tic/subscriptions",
      "organizations_url": "https://api.github.com/users/p12tic/orgs",
      "repos_url": "https://api.github.com/users/p12tic/repos",
      "events_url": "https://api.github.com/users/p12tic/events{/privacy}",
      "received_events_url": "https://api.github.com/users/p12tic/received_events",
      "type": "User",
      "site_admin": false
    },
    "prerelease": false,
    "created_at": "2020-06-06T18:19:19Z",
    "published_at": "2020-06-06T18:21:36Z",
    "assets": [],
    "tarball_url": "https://api.github.com/repos/buildbot/buildbot/tarball/v2.8.1",
    "zipball_url": "https://api.github.com/repos/buildbot/buildbot/zipball/v2.8.1",
    "body": "- Fix source distribution missing required buildbot.test.fakedb module for unit tests.\\r\\n- Fix crash in trigger step when renderables are used for scheduler names (#5312)\\r\\n"
  }
]
"""

apiCommitv282 = """
{
  "sha": "2600f7d39ccecc804ab68fe985db6ecf6c545434",
  "node_id": "MDY6Q29tbWl0NzYwMTY1OjI2MDBmN2QzOWNjZWNjODA0YWI2OGZlOTg1ZGI2ZWNmNmM1NDU0MzQ=",
  "commit": {
    "author": {
      "name": "Povilas Kanapickas",
      "email": "povilas@radix.lt",
      "date": "2020-06-14T14:22:56Z"
    },
    "committer": {
      "name": "GitHub",
      "email": "noreply@github.com",
      "date": "2020-06-14T14:22:56Z"
    },
    "message": "Merge pull request #5359 from p12tic/release-notes\\n\\nRelease notes for 2.8.2",
    "tree": {
      "sha": "bdc29670315ac8020c65bac302c54fd0e21aca5a",
      "url": "https://api.github.com/repos/buildbot/buildbot/git/trees/bdc29670315ac8020c65bac302c54fd0e21aca5a"
    },
    "url": "https://api.github.com/repos/buildbot/buildbot/git/commits/2600f7d39ccecc804ab68fe985db6ecf6c545434",
    "comment_count": 0,
    "verification": {}
  },
  "url": "https://api.github.com/repos/buildbot/buildbot/commits/2600f7d39ccecc804ab68fe985db6ecf6c545434",
  "html_url": "https://github.com/buildbot/buildbot/commit/2600f7d39ccecc804ab68fe985db6ecf6c545434",
  "comments_url": "https://api.github.com/repos/buildbot/buildbot/commits/2600f7d39ccecc804ab68fe985db6ecf6c545434/comments",
  "author": {
    "login": "p12tic",
    "id": 1056711,
    "node_id": "MDQ6VXNlcjEwNTY3MTE=",
    "avatar_url": "https://avatars0.githubusercontent.com/u/1056711?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/p12tic",
    "html_url": "https://github.com/p12tic",
    "followers_url": "https://api.github.com/users/p12tic/followers",
    "following_url": "https://api.github.com/users/p12tic/following{/other_user}",
    "gists_url": "https://api.github.com/users/p12tic/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/p12tic/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/p12tic/subscriptions",
    "organizations_url": "https://api.github.com/users/p12tic/orgs",
    "repos_url": "https://api.github.com/users/p12tic/repos",
    "events_url": "https://api.github.com/users/p12tic/events{/privacy}",
    "received_events_url": "https://api.github.com/users/p12tic/received_events",
    "type": "User",
    "site_admin": false
  },
  "committer": {
    "login": "web-flow",
    "id": 19864447,
    "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
    "avatar_url": "https://avatars3.githubusercontent.com/u/19864447?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/web-flow",
    "html_url": "https://github.com/web-flow",
    "followers_url": "https://api.github.com/users/web-flow/followers",
    "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
    "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
    "organizations_url": "https://api.github.com/users/web-flow/orgs",
    "repos_url": "https://api.github.com/users/web-flow/repos",
    "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
    "received_events_url": "https://api.github.com/users/web-flow/received_events",
    "type": "User",
    "site_admin": false
  },
  "parents": [
    {
      "sha": "f3f43cd08bb21e672fddfbb05104098f2bb7e266",
      "url": "https://api.github.com/repos/buildbot/buildbot/commits/f3f43cd08bb21e672fddfbb05104098f2bb7e266",
      "html_url": "https://github.com/buildbot/buildbot/commit/f3f43cd08bb21e672fddfbb05104098f2bb7e266"
    },
    {
      "sha": "ea33b3301f9d9602afce4f46afa4b64d293e0c09",
      "url": "https://api.github.com/repos/buildbot/buildbot/commits/ea33b3301f9d9602afce4f46afa4b64d293e0c09",
      "html_url": "https://github.com/buildbot/buildbot/commit/ea33b3301f9d9602afce4f46afa4b64d293e0c09"
    }
  ],
  "stats": {
    "total": 10,
    "additions": 9,
    "deletions": 1
  },
  "files": [
    {
      "sha": "9ae7fdad460d6f1c041422c2dac60d62b5b24fc8",
      "filename": "master/buildbot/newsfragments/windows-service-crash.bugfix",
      "status": "removed",
      "additions": 0,
      "deletions": 1,
      "changes": 1,
      "blob_url": "https://github.com/buildbot/buildbot/blob/f3f43cd08bb21e672fddfbb05104098f2bb7e266/master/buildbot/newsfragments/windows-service-crash.bugfix",
      "raw_url": "https://github.com/buildbot/buildbot/raw/f3f43cd08bb21e672fddfbb05104098f2bb7e266/master/buildbot/newsfragments/windows-service-crash.bugfix",
      "contents_url": "https://api.github.com/repos/buildbot/buildbot/contents/master/buildbot/newsfragments/windows-service-crash.bugfix?ref=f3f43cd08bb21e672fddfbb05104098f2bb7e266",
      "patch": "@@ -1 +0,0 @@\\n-Fix crash in Buildbot Windows service startup code (:issue:`5344`)"
    },
    {
      "sha": "0a32cdaf658ac4dbc27d40a95284a1f689350b28",
      "filename": "master/docs/relnotes/index.rst",
      "status": "modified",
      "additions": 9,
      "deletions": 0,
      "changes": 9,
      "blob_url": "https://github.com/buildbot/buildbot/blob/2600f7d39ccecc804ab68fe985db6ecf6c545434/master/docs/relnotes/index.rst",
      "raw_url": "https://github.com/buildbot/buildbot/raw/2600f7d39ccecc804ab68fe985db6ecf6c545434/master/docs/relnotes/index.rst",
      "contents_url": "https://api.github.com/repos/buildbot/buildbot/contents/master/docs/relnotes/index.rst?ref=2600f7d39ccecc804ab68fe985db6ecf6c545434",
      "patch": "@@ -10,6 +10,15 @@ Release Notes\\n \\n .. towncrier release notes start\\n \\n+Buildbot ``2.8.2`` ( ``2020-06-14`` )\\n+=====================================\\n+\\n+Bug fixes\\n+---------\\n+\\n+- Fix crash in Buildbot Windows service startup code (:issue:`5344`)\\n+\\n+\\n Buildbot ``2.8.1`` ( ``2020-06-06`` )\\n =====================================\\n "
    }
  ]
}
"""

apiCommitv281 = """
{
  "sha": "3291dbbeebb6a5ca6e91785ade2da6e0a991cb5d",
  "node_id": "MDY6Q29tbWl0NzYwMTY1OjMyOTFkYmJlZWJiNmE1Y2E2ZTkxNzg1YWRlMmRhNmUwYTk5MWNiNWQ=",
  "commit": {
    "author": {
      "name": "Povilas Kanapickas",
      "email": "povilas@radix.lt",
      "date": "2020-06-06T18:18:42Z"
    },
    "committer": {
      "name": "GitHub",
      "email": "noreply@github.com",
      "date": "2020-06-06T18:18:42Z"
    },
    "message": "Merge pull request #5327 from p12tic/2.8.x-release\\n\\nrelnotes for 2.8.1",
    "tree": {
      "sha": "83f5f1ed1c60fbdf8d1016b6e42ba4f908a2bae5",
      "url": "https://api.github.com/repos/buildbot/buildbot/git/trees/83f5f1ed1c60fbdf8d1016b6e42ba4f908a2bae5"
    },
    "url": "https://api.github.com/repos/buildbot/buildbot/git/commits/3291dbbeebb6a5ca6e91785ade2da6e0a991cb5d",
    "comment_count": 0,
    "verification": {
      "verified": true,
      "reason": "valid",
      "signature": "-----BEGIN PGP SIGNATURE-----\\n\\nwsBcBAABCAAQBQJe294CCRBK7hj4Ov3rIwAAdHIIAK45nhDHIp3mo+If0Nkov2Nk\\nZlJ0ATKWC8ejUsKwOYf09w1x911lwcBJYtMqyu0djWqnf4Qjz818otnvt4UTXzf1\\n1IJa5s3Uv86nLZTfj1Iyc6acmsK7NyMvlQXWdJhH1ZvBpeCWCpaadCheJGWYedh4\\nA1AW8HweUfgKKBZdjsqIvyWA3u596S9pN/vGDhFNMnGtwtXPROXRDVPSQjbzEtzU\\nimGMFXKCnwbEp/UDmQ+cCPMC8U0oYEYtMtGzY1K/lgLnEcTPMiMkL26t7X0YfBuG\\ntF6SW1yPPwp1zzKz021OB7z4IWBO2+HiyBwA7jMOj+D2zOvW3xvTMXwVQALPw7Q=\\n=Xc37\\n-----END PGP SIGNATURE-----\\n",
      "payload": "tree 83f5f1ed1c60fbdf8d1016b6e42ba4f908a2bae5\\nparent 2eec2932a14d565d0de669cc20152c754c09b22f\\nparent dbfe3cdc486502f54f90e430da2400670e78e9bf\\nauthor Povilas Kanapickas <povilas@radix.lt> 1591467522 +0300\\ncommitter GitHub <noreply@github.com> 1591467522 +0300\\n\\nMerge pull request #5327 from p12tic/2.8.x-release\\n\\nrelnotes for 2.8.1"
    }
  },
  "url": "https://api.github.com/repos/buildbot/buildbot/commits/3291dbbeebb6a5ca6e91785ade2da6e0a991cb5d",
  "html_url": "https://github.com/buildbot/buildbot/commit/3291dbbeebb6a5ca6e91785ade2da6e0a991cb5d",
  "comments_url": "https://api.github.com/repos/buildbot/buildbot/commits/3291dbbeebb6a5ca6e91785ade2da6e0a991cb5d/comments",
  "author": {
    "login": "p12tic",
    "id": 1056711,
    "node_id": "MDQ6VXNlcjEwNTY3MTE=",
    "avatar_url": "https://avatars0.githubusercontent.com/u/1056711?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/p12tic",
    "html_url": "https://github.com/p12tic",
    "followers_url": "https://api.github.com/users/p12tic/followers",
    "following_url": "https://api.github.com/users/p12tic/following{/other_user}",
    "gists_url": "https://api.github.com/users/p12tic/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/p12tic/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/p12tic/subscriptions",
    "organizations_url": "https://api.github.com/users/p12tic/orgs",
    "repos_url": "https://api.github.com/users/p12tic/repos",
    "events_url": "https://api.github.com/users/p12tic/events{/privacy}",
    "received_events_url": "https://api.github.com/users/p12tic/received_events",
    "type": "User",
    "site_admin": false
  },
  "committer": {
    "login": "web-flow",
    "id": 19864447,
    "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
    "avatar_url": "https://avatars3.githubusercontent.com/u/19864447?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/web-flow",
    "html_url": "https://github.com/web-flow",
    "followers_url": "https://api.github.com/users/web-flow/followers",
    "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
    "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
    "organizations_url": "https://api.github.com/users/web-flow/orgs",
    "repos_url": "https://api.github.com/users/web-flow/repos",
    "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
    "received_events_url": "https://api.github.com/users/web-flow/received_events",
    "type": "User",
    "site_admin": false
  },
  "parents": [
    {
      "sha": "2eec2932a14d565d0de669cc20152c754c09b22f",
      "url": "https://api.github.com/repos/buildbot/buildbot/commits/2eec2932a14d565d0de669cc20152c754c09b22f",
      "html_url": "https://github.com/buildbot/buildbot/commit/2eec2932a14d565d0de669cc20152c754c09b22f"
    },
    {
      "sha": "dbfe3cdc486502f54f90e430da2400670e78e9bf",
      "url": "https://api.github.com/repos/buildbot/buildbot/commits/dbfe3cdc486502f54f90e430da2400670e78e9bf",
      "html_url": "https://github.com/buildbot/buildbot/commit/dbfe3cdc486502f54f90e430da2400670e78e9bf"
    }
  ],
  "stats": {
    "total": 13,
    "additions": 10,
    "deletions": 3
  },
  "files": [
    {
      "sha": "e9eb8431559c6868226d8a0c21fa979d18afe333",
      "filename": "master/buildbot/newsfragments/sdist_fakedb.bugfix",
      "status": "removed",
      "additions": 0,
      "deletions": 1,
      "changes": 1,
      "blob_url": "https://github.com/buildbot/buildbot/blob/2eec2932a14d565d0de669cc20152c754c09b22f/master/buildbot/newsfragments/sdist_fakedb.bugfix",
      "raw_url": "https://github.com/buildbot/buildbot/raw/2eec2932a14d565d0de669cc20152c754c09b22f/master/buildbot/newsfragments/sdist_fakedb.bugfix",
      "contents_url": "https://api.github.com/repos/buildbot/buildbot/contents/master/buildbot/newsfragments/sdist_fakedb.bugfix?ref=2eec2932a14d565d0de669cc20152c754c09b22f",
      "patch": "@@ -1 +0,0 @@\\n-Fixed source distribution missing required buildbot.test.fakedb module for unit tests.\\n"
    },
    {
      "sha": "2d4dfb39933f100d205de2e058159bb862e87ce0",
      "filename": "master/buildbot/newsfragments/trigger.bugfix",
      "status": "removed",
      "additions": 0,
      "deletions": 2,
      "changes": 2,
      "blob_url": "https://github.com/buildbot/buildbot/blob/2eec2932a14d565d0de669cc20152c754c09b22f/master/buildbot/newsfragments/trigger.bugfix",
      "raw_url": "https://github.com/buildbot/buildbot/raw/2eec2932a14d565d0de669cc20152c754c09b22f/master/buildbot/newsfragments/trigger.bugfix",
      "contents_url": "https://api.github.com/repos/buildbot/buildbot/contents/master/buildbot/newsfragments/trigger.bugfix?ref=2eec2932a14d565d0de669cc20152c754c09b22f",
      "patch": "@@ -1,2 +0,0 @@\\n-fix crash in trigger step when renderables are used for scheduler names (:issue:`5312`)\\n-"
    },
    {
      "sha": "ac77e06744a44483e7ec16dcc30dff2c19e335af",
      "filename": "master/docs/relnotes/index.rst",
      "status": "modified",
      "additions": 10,
      "deletions": 0,
      "changes": 10,
      "blob_url": "https://github.com/buildbot/buildbot/blob/3291dbbeebb6a5ca6e91785ade2da6e0a991cb5d/master/docs/relnotes/index.rst",
      "raw_url": "https://github.com/buildbot/buildbot/raw/3291dbbeebb6a5ca6e91785ade2da6e0a991cb5d/master/docs/relnotes/index.rst",
      "contents_url": "https://api.github.com/repos/buildbot/buildbot/contents/master/docs/relnotes/index.rst?ref=3291dbbeebb6a5ca6e91785ade2da6e0a991cb5d",
      "patch": "@@ -10,6 +10,16 @@ Release Notes\\n \\n .. towncrier release notes start\\n \\n+Buildbot ``2.8.1`` ( ``2020-06-06`` )\\n+=====================================\\n+\\n+Bug fixes\\n+---------\\n+\\n+- Fix source distribution missing required buildbot.test.fakedb module for unit tests.\\n+- Fix crash in trigger step when renderables are used for scheduler names (:issue:`5312`)\\n+\\n+\\n Buildbot ``2.8.0`` ( ``2020-05-27`` )\\n =====================================\\n "
    }
  ]
}
"""

author1 = """{
  "login": "p12tic",
  "id": 1056711,
  "node_id": "MDQ6VXNlcjEwNTY3MTE=",
  "avatar_url": "https://avatars0.githubusercontent.com/u/1056711?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/p12tic",
  "html_url": "https://github.com/p12tic",
  "followers_url": "https://api.github.com/users/p12tic/followers",
  "following_url": "https://api.github.com/users/p12tic/following{/other_user}",
  "gists_url": "https://api.github.com/users/p12tic/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/p12tic/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/p12tic/subscriptions",
  "organizations_url": "https://api.github.com/users/p12tic/orgs",
  "repos_url": "https://api.github.com/users/p12tic/repos",
  "events_url": "https://api.github.com/users/p12tic/events{/privacy}",
  "received_events_url": "https://api.github.com/users/p12tic/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Povilas Kanapickas",
  "company": null,
  "blog": "",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": null,
  "twitter_username": null,
  "public_repos": 68,
  "public_gists": 3,
  "followers": 84,
  "following": 2,
  "created_at": "2011-09-16T18:15:27Z",
  "updated_at": "2020-08-10T17:24:29Z"
}"""


class GithubApiTestCase(changesource.ChangeSourceMixin,
                        TestReactorMixin,
                        unittest.TestCase) :

    @defer.inlineCallbacks
    def setUp(self) :
        self.setUpTestReactor()
        yield self.setUpChangeSource()
        yield self.master.startService()

        token = '6121770b1c4c11cdf4450561d90db3605d6486103fc5c7ecd6b441a085eaebdc'

        headers = {
            'User-Agent': 'Buildbot',
            'Authorization': 'token ' + token
        }

        self._http = yield fakehttpclientservice.HTTPClientService.getFakeService(
            self.master, self, "https://api.github.com", headers=headers, debug=True)

        self.changesource = changes.GitHubAPI("buildbot", "buildbot", project="proj", token=token, pollInterval=300)

        yield self.changesource.setServiceParent(self.master)

    @defer.inlineCallbacks
    def tearDown(self):
        yield self.tearDownChangeSource()
        yield self.master.stopService()

    @defer.inlineCallbacks
    def test_fetch_releases(self) :

        self._http.expect(
            method='get',
            ep='/repos/buildbot/buildbot/releases',
            content_json=json.loads(apiRepoList))

        self._http.expect(
            method='get',
            ep='/repos/buildbot/buildbot/commits/v2.8.2',
            content_json=json.loads(apiCommitv282))

        self._http.expect(
            method='get',
            ep='/users/p12tic',
            content_json=json.loads(author1))

        self._http.expect(
            method='get',
            ep='/repos/buildbot/buildbot/commits/v2.8.1',
            content_json=json.loads(apiCommitv281))

        self._http.expect(
            method='get',
            ep='/users/p12tic',
            content_json=json.loads(author1))

        yield self.changesource.poll()
