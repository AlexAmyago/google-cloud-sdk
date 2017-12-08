# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command to list all project IDs associated with the active user."""

import textwrap
from googlecloudsdk.api_lib.projects import projects_api
from googlecloudsdk.api_lib.projects import util
from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.BETA, base.ReleaseTrack.GA)
class List(util.ProjectCommand, base.ListCommand):
  """List projects accessible by the active account.

  Lists all active projects, where the active account has Owner, Editor or
  Viewer permissions. Projects are listed in alphabetical order by project name.
  Projects that have been deleted or are pending deletion are not included.

  You can specify the maximum number of projects to list using the `--limit`
  flag.
  """

  detailed_help = {
      'EXAMPLES': textwrap.dedent("""\
          The following command lists a maximum of five projects sorted
          alphabetically by name:

            $ {command} --limit=5
      """),
  }

  @util.HandleHttpError
  def Run(self, args):
    """Run the list command."""

    projects_client = util.GetClient()
    messages = util.GetMessages()
    # TODO(user): b/27946801 handle --limit,--page-size,--filter
    return projects_api.List(client=projects_client, messages=messages)
