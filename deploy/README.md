# Deployment

You can deploy the application using [kustomize](https://kustomize.io/). The `kustomize` folder contains all the kubernetes manifests file along with `kustomize/kustomization.yaml` file.

#### Run the following command to deploy on target Kubernetes cluster

```bash
kustomize build . | kubectl apply -f -
```

#### Testing out service autoscaling

You can run a small brute-force test for the service endpoint to increase the CPU consumption & scale out the service. The HPA is configured to scale the service if the `targetCPUUtilizationPercentage` hits 50%.

NOTE: You may need to have [metrics-server](https://github.com/kubernetes-sigs/metrics-server) running in your kubernetes cluster.

```bash
hey -n 10000 -c 2 -t 20 -q 50 -m GET -H "Accept: text/html" http://KUBERNETES_SERVICE_IP:8000
```

Where, `KUBERNETES_SERVICE_IP` is the IP address of the service `timestamp-service` in `vector` namespace.

```bash
kubectl get svc -n vector
```

[hey](https://github.com/rakyll/hey) is the HTTP load testing tool, similar to apache ab tool.
