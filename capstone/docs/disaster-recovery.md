# PLAT-118 — ShopSphere Disaster Recovery Runbook

## Environment
- Namespace: shopsphere-dev
- StatefulSet: shopsphere-database
- Database: shopsphere
- MySQL version: 8.4
- PVC: mysql-storage-shopsphere-database-0
- Storage capacity: 5Gi

## Backup Strategy
- Backup type: MySQL logical backup
- Tool: mysqldump
- Backup location: capstone/backups/ (local lab only)
- Consistency: --single-transaction
- Integrity check: SHA-256 checksum

## Recovery Procedure
1. Identify the affected database and determine the incident scope.
2. Locate and verify the latest valid backup.
3. Provision an isolated MySQL recovery environment.
4. Restore the SQL dump.
5. Verify database schema and record counts.
6. Perform application-level validation before returning to service.

## Recovery Test Results
- Original products: 3
- Records after simulated deletion: 0
- Records after restoration: 3
- Recovery status: PASSED
- Original Kubernetes database: Unchanged

## RPO and RTO
- RPO: Not formally established.
- RTO: Not formally established.
- Both require business-defined targets and measured testing.

## Production Improvements
- Automate scheduled backups.
- Encrypt backups at rest and in transit.
- Store backups outside the Kubernetes cluster.
- Apply retention and access-control policies.
- Monitor backup failures.
- Perform periodic restore testing.
- Consider point-in-time recovery using MySQL binary logs.
