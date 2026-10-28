# Repository agent instructions

## GitHub account

- All agent-performed GitHub operations for this repository must use the `dwhao84` account only. Do not use another personal, shared, or bot account.
- Before creating commits or making remote changes (including push, branches, pull requests, issues, or releases), verify that the authenticated GitHub account is `dwhao84` (for GitHub CLI, run `gh api user --jq .login`). Ensure the Git transport or connector used for the operation authenticates as the same account.
- If the account is different or cannot be verified, stop the affected operation and ask the user to authenticate as `dwhao84`. Never silently switch to another account.
- Agent-created commits must use author and committer name `dwhao84` and a GitHub-verified email belonging to that account, such as `100706617+dwhao84@users.noreply.github.com`. Configure identity locally for this repository; do not change global Git settings.
- Never act or submit changes in anyone else's name. Do not use another person's identity, a bot identity, an alternate author/committer, or a `Co-authored-by` attribution for another identity.
- All generated deployment commits must also use `dwhao84` as author and committer. There is no exception for bot commit identities.
- GitHub Actions may use its repository-scoped workflow token to run the authorized deployment; this token is automation infrastructure, not authentication as the personal `dwhao84` account. Do not claim otherwise or introduce another person's credentials.
