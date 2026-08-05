                        GitHub PR
                            │
                     push new commit
                            │
                            ▼
                    ┌───────────────┐
                    │ GitHub Actions│
                    └───────┬───────┘
                            │
                            ▼
                    Terraform Apply
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
            VPC             EC2           SG
                            │
                            ▼
                     Wait for SSH
                            │
                            ▼
                     Ansible Playbook
                            │
                   ┌────────┴────────┐
                   ▼                 ▼
              Deploy ECU          Tests
                   │                 │
                   └────────┬────────┘
                            ▼
                     Capture results
                            │
                            ▼
                      PR Comment
                            │
                            ▼
                  Terraform Destroy
                            │
                            ▼
                     AWS = clean