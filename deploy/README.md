# Deployment

You can deploy the application using [kustomize](https://kustomize.io/). The `kustomize` folder contains all the kubernetes manifests file along with `kustomize/kustomization.yaml` file.

#### Run the following command to deploy on target Kubernetes cluster

```bash
kustomize build . | kubectl apply -f -
```
