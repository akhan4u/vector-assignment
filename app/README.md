# Creating the Dockerfile

### Observations

1. My first thought was to create the Dockerfile with bare minimum size.
2. Container with scratch as base image are less in size and better in-terms of security
3. I can't use python application in scratch based Docker Base Image, hence using google's [distroless](https://stackoverflow.com/questions/62581924/is-there-a-way-to-compile-a-python-program-to-binary-and-use-it-with-a-scratch-d) as container base image.
4. Python alpine image is also a close match to distroless image in terms of the uncompressed size on disk.

```bash
python                                                                                        3.10-alpine          4da4c1dc8c72   3 weeks ago     48.7MB
gcr.io/distroless/python3-debian10                                                            latest               54c465bcd58f   52 years ago    48.3MB
```
5. Instead of tagging image with `latest` tag, used the tag sha.
