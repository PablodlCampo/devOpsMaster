Etapa 1 — Fundamentos AWS + IaC (semanas 1–6)
API básica con subida a S3, Terraform con remote state en S3 + DynamoDB locking, GitHub Actions desplegando en EC2. Certificación objetivo: AWS Cloud Practitioner CLF-C02 en la semana 5. Es la base conceptual que hace que todo lo demás tenga sentido.

Etapa 2 — CI/CD avanzado + entornos + BD real (semanas 7–13)
Se integra el LLM real, PostgreSQL en RDS, pipeline multi-stage con staging y producción separados vía Terraform Workspaces. Se añaden pre-commit hooks y gestión de migraciones en la pipeline. Certificación objetivo: SAA-C03. Estudiarlo mientras construyes la arquitectura es la mejor preparación posible.

Etapa 3 — Observabilidad + seguridad cloud (semanas 14–20)
CloudWatch con anomaly detection, X-Ray para trazas, GuardDuty, Security Hub, AWS Config para compliance continuo. El código añade structured logging con correlation IDs y métricas de negocio. Certificación objetivo: Developer Associate DVA-C02, que cubre X-Ray, CodePipeline y Lambda.

Etapa 4 — Microservicios + ECS Fargate + BD vectorial (semanas 21–31)
El salto grande en código: dividir la app en cuatro microservicios reales (api-gateway, upload-worker, query-engine, exam-generator) con SQS entre ellos. En infraestructura: ECS Fargate, ECR con Trivy para escaneo de imágenes, blue/green con CodeDeploy. Certificación objetivo: DevOps Engineer Professional DOP-C02, la más relevante de todo el plan.

Etapa 5 — Kubernetes: EKS + Helm + GitOps (semanas 32–42)
Migración de ECS a EKS, Helm para gestión de releases, ArgoCD para GitOps completo, KEDA para escalar pods basándose en la profundidad de la cola SQS, OPA Gatekeeper para políticas de seguridad. Certificación objetivo: CKA. El trabajo diario en EKS es prácticamente el examen.

Etapa 6 — Multi-cloud: Azure + Terragrunt + Istio (semanas 43–49)
Un servicio de notificaciones se despliega en AKS con Azure Service Bus, autenticación federada entre AWS y Azure vía OIDC, Terragrunt para gestionar módulos multi-cloud, Istio para mTLS entre todos los servicios y canary releases. Certificaciones objetivo: AZ-104 y AZ-400.

Etapa 7 — SRE: chaos, FinOps y madurez (semanas 50–52)
Stack LGTM propio (Prometheus + Grafana + Loki + Tempo), SLOs con error budgets, Chaos Mesh o AWS FIS para chaos engineering, k6 para tests de carga, plan de DR probado en producción.