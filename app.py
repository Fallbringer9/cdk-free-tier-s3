#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_free_tier_s3.cdk_free_tier_s3_stack import CdkFreeTierS3Stack


app = cdk.App()

env = cdk.Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"),
    region=os.getenv("CDK_DEFAULT_REGION") or "eu-west-3",
)

CdkFreeTierS3Stack(app, "CdkFreeTierS3Stack", env=env)

app.synth()
