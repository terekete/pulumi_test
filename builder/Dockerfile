FROM python

COPY . .

# Download and install required tools.
RUN curl -L https://get.pulumi.com/ | bash
RUN pip3 install --upgrade pulumi>=3.0.0,<4.0.0
RUN pip3 install --upgrade pulumi-gcp>=5.0.0,<6.0.0


ENV PATH=$PATH:/root/.pulumi/bin

ENTRYPOINT [ "pulumi", "version" ]