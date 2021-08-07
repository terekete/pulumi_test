FROM python

COPY . .

# Download and install required tools.
RUN curl -L https://get.pulumi.com/ | bash
RUN pip3 install --upgrade pulumi
RUN pip3 install --upgrade pulumi-gcp
RUN pip3 install --upgrade Cerberus


ENV PATH=$PATH:/root/.pulumi/bin

ENTRYPOINT [ "pulumi", "version" ]