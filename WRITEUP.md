Analyze, choose, and justify the appropriate resource option for deploying the app.

Cost
VM:
  Pay for compute 24/7, even when idle.
  Must manage OS, security updates, and all dependencies.
  Cheapest VM is still more expensive than App Service Free/B1 for a small app.
App Service:
  Free F1 (where available) or low-cost Basic B1.
  Platform handles OS, SSL, scaling, and patching.
  No cost when stopped; lower total cost of ownership for small workloads.

Scalability
VM:
  Manual scaling (resize VM, add load balancer, etc.).
  More effort and complexity for high availability.
App Service:
  Built-in vertical and horizontal scaling.
  Autoscale and staging slots available on higher tiers.

Availability
VM:
  Single VM is a single point of failure unless you architect for redundancy.
  You are responsible for patching, monitoring, and failover.
App Service:
  Platform-managed availability, health probes, and rolling updates.
  Higher uptime with less effort.

Workflow
VM:
  Full control over OS and stack, but must configure everything (Nginx, SSL, ODBC, etc.).
  CI/CD setup is manual.
App Service:
  GitHub Actions and Deployment Center for easy CI/CD.
  Environment variables, logs, and scaling are managed in the portal.

Choice & Justification
I chose App Service because it is lower cost, easier to deploy, and requires less maintenance for a small Flask app. The platform handles scaling, SSL, and availability, letting me focus on the application code.

Assess app changes that would change your decision.
If the app required:
  Custom OS-level configuration, background services, or specialized software not supported by App Service,
  Strict networking or compliance needs (private endpoints, custom routing),
  Or if I needed to run workloads not supported by App Service (e.g., persistent daemons, custom containers)

…then I would consider deploying on a VM or using Azure Container Apps/AKS for more control. For this project’s needs, App Service is the best fit.


Resource summary
Resource Group: cms-rg
App Service: cmswebapp
  Python 3.10
  Startup command: gunicorn --bind=0.0.0.0:$PORT application:app
App Service Plan: Free F1 (with a brief temporary switch to Basic B1 when daily usage limit was reached)
SQL Server: cms-sql-server.database.windows.net
SQL Database: cms-db
Storage Account: cmsstoragejr
  Blob Container: images
  Access level: Container
Microsoft Entra ID App Registration:
  Client ID: 28756dcc-e0e5-47d0-acdc-5430b8354bfe
  Redirect URI: https://cmswebapp.azurewebsites.net/getAToken
Logging:
  App Service Log stream shows both invalid and successful login attempts
Region(s):
  Most resources deployed in West US (closest to my location for lower latency).
  Some resources (App Service Plan, App Service, Managed Identity) deployed in West US 2 due to lower cost or quota availability.

Note:
Free F1 plan was used initially, but due to daily usage limits, the deployment was moved to Basic B1 to complete the project.
West US was chosen for proximity, but West US 2 was used for some resources because it offered lower rates and/or available quotas at the time of deployment.
