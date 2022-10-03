# Copy the virtualenv into a distroless image
FROM gcr.io/distroless/python3-debian10@sha256:b0041237ec3b3009275c1e0698fd7339940f2736d3359874da71bebd0878ed0a
COPY . /app
WORKDIR /app
ENTRYPOINT ["/usr/bin/python3.7", "print_timestamp.py"]
