# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer
from .validators.opsworkscm import validate_tags_or_list


class EngineAttribute(AWSProperty):
    """
    `EngineAttribute <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworkscm-server-engineattribute.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class Server(AWSObject):
    """
    `Server <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html>`__
    """

    resource_type = "AWS::OpsWorksCM::Server"

    props: PropsDictType = {
        "AssociatePublicIpAddress": (boolean, False),
        "BackupId": (str, False),
        "BackupRetentionCount": (integer, False),
        "CustomCertificate": (str, False),
        "CustomDomain": (str, False),
        "CustomPrivateKey": (str, False),
        "DisableAutomatedBackup": (boolean, False),
        "Engine": (str, False),
        "EngineAttributes": ([EngineAttribute], False),
        "EngineModel": (str, False),
        "EngineVersion": (str, False),
        "InstanceProfileArn": (str, True),
        "InstanceType": (str, True),
        "KeyPair": (str, False),
        "PreferredBackupWindow": (str, False),
        "PreferredMaintenanceWindow": (str, False),
        "SecurityGroupIds": ([str], False),
        "ServerName": (str, False),
        "ServiceRoleArn": (str, True),
        "SubnetIds": ([str], False),
        "Tags": (validate_tags_or_list, False),
    }
