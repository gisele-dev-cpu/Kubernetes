# PLAT-119: Kubernetes Runtime Threat Detection with Falco

## Objective
Implement runtime security monitoring using Falco and modern eBPF.

## Environment
- Kubernetes: Minikube
- Falco: 0.45.2
- Helm chart: 9.2.2
- Driver: modern_ebpf

## Implementation
1. Installed Falco using Helm as a Kubernetes DaemonSet.
2. Enabled JSON security alerts.
3. Verified the built-in Terminal shell in container rule.
4. Created a custom rule to detect shell execution in runtime-lab.
5. Deployed the custom rule using Helm.
6. Verified detection of non-interactive shell execution.

## Custom Detection
Rule: Shell Execution in Runtime Lab

Condition:
- Process execution inside a container
- Namespace equals runtime-lab
- Process name is sh, bash, or ash

Severity: WARNING

## Validation
Executed:

kubectl exec -n runtime-lab runtime-test -- /bin/sh -c 'id'

Falco successfully generated a Warning alert containing:
- Process name and command
- Username
- Kubernetes Pod and namespace
- Container metadata

## Security Takeaways
- Admission control prevents prohibited workload configurations.
- Runtime detection identifies suspicious behavior after deployment.
- Falco observes Linux system calls through eBPF.
- Falco generates alerts but does not automatically block execution.
- Custom rules enable workload-specific detection engineering.

## Production Considerations
- Forward alerts to a SIEM.
- Tune detection rules to reduce false positives.
- Monitor Falco agent health and event drops.
- Manage rules through GitOps and Helm.
