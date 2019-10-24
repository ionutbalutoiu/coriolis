# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.

EXECUTION_STATUS_RUNNING = "RUNNING"
EXECUTION_STATUS_COMPLETED = "COMPLETED"
EXECUTION_STATUS_ERROR = "ERROR"

TASK_STATUS_PENDING = "PENDING"
TASK_STATUS_RUNNING = "RUNNING"
TASK_STATUS_COMPLETED = "COMPLETED"
TASK_STATUS_ERROR = "ERROR"
TASK_STATUS_CANCELED = "CANCELED"
TASK_STATUS_CANCELED_FOR_DEBUGGING = "CANCELED_FOR_DEBUGGING"
TASK_STATUS_ON_ERROR_ONLY = "EXECUTE_ON_ERROR_ONLY"

TASK_TYPE_EXPORT_INSTANCE = "EXPORT_INSTANCE"
TASK_TYPE_IMPORT_INSTANCE = "IMPORT_INSTANCE"
TASK_TYPE_FINALIZE_IMPORT_INSTANCE = "FINALIZE_IMPORT_INSTANCE"
TASK_TYPE_CLEANUP_FAILED_IMPORT_INSTANCE = "CLEANUP_FAILED_IMPORT_INSTANCE"

TASK_TYPE_DEPLOY_DISK_COPY_RESOURCES = "DEPLOY_DISK_COPY_RESOURCES"
TASK_TYPE_COPY_DISK_DATA = "COPY_DISK_DATA"
TASK_TYPE_DELETE_DISK_COPY_RESOURCES = "DELETE_DISK_COPY_RESOURCES"

TASK_TYPE_DEPLOY_MIGRATION_SOURCE_RESOURCES = (
    "DEPLOY_MIGRATION_SOURCE_RESOURCES")
TASK_TYPE_DEPLOY_MIGRATION_TARGET_RESOURCES = (
    "DEPLOY_MIGRATION_TARGET_RESOURCES")
TASK_TYPE_DELETE_MIGRATION_SOURCE_RESOURCES = (
    "DELETE_MIGRATION_SOURCE_RESOURCES")
TASK_TYPE_DELETE_MIGRATION_TARGET_RESOURCES = (
    "DELETE_MIGRATION_TARGET_RESOURCES")
TASK_TYPE_DEPLOY_INSTANCE_RESOURCES = "DEPLOY_INSTANCE_RESOURCES"
TASK_TYPE_FINALIZE_INSTANCE_DEPLOYMENT = "FINALIZE_INSTANCE_DEPLOYMENT"
TASK_TYPE_CLEANUP_FAILED_INSTANCE_DEPLOYMENT = (
    "CLEANUP_FAILED_INSTANCE_DEPLOYMENT")
TASK_TYPE_CLEANUP_INSTANCE_STORAGE = "CLEANUP_INSTANCE_STORAGE"

TASK_TYPE_CREATE_INSTANCE_DISKS = "CREATE_INSTANCE_DISKS"

TASK_TYPE_DEPLOY_OS_MORPHING_RESOURCES = "DEPLOY_OS_MORPHING_RESOURCES"
TASK_TYPE_OS_MORPHING = "OS_MORPHING"
TASK_TYPE_DELETE_OS_MORPHING_RESOURCES = "DELETE_OS_MORPHING_RESOURCES"


TASK_TYPE_GET_INSTANCE_INFO = "GET_INSTANCE_INFO"
TASK_TYPE_DEPLOY_REPLICA_DISKS = "DEPLOY_REPLICA_DISKS"
TASK_TYPE_DELETE_REPLICA_DISKS = "DELETE_REPLICA_DISKS"
TASK_TYPE_REPLICATE_DISKS = "REPLICATE_DISKS"
TASK_TYPE_DEPLOY_REPLICA_SOURCE_RESOURCES = "DEPLOY_REPLICA_SOURCE_RESOURCES"
TASK_TYPE_DELETE_REPLICA_SOURCE_RESOURCES = "DELETE_REPLICA_SOURCE_RESOURCES"
TASK_TYPE_DEPLOY_REPLICA_TARGET_RESOURCES = "DEPLOY_REPLICA_TARGET_RESOURCES"
TASK_TYPE_DELETE_REPLICA_TARGET_RESOURCES = "DELETE_REPLICA_TARGET_RESOURCES"
TASK_TYPE_SHUTDOWN_INSTANCE = "SHUTDOWN_INSTANCE"
TASK_TYPE_DEPLOY_REPLICA_INSTANCE = "DEPLOY_REPLICA_INSTANCE"
TASK_TYPE_FINALIZE_REPLICA_INSTANCE_DEPLOYMENT = (
    "FINALIZE_REPLICA_INSTANCE_DEPLOYMENT")
TASK_TYPE_CLEANUP_FAILED_REPLICA_INSTANCE_DEPLOYMENT = (
    "CLEANUP_FAILED_REPLICA_INSTANCE_DEPLOYMENT")
TASK_TYPE_CREATE_REPLICA_DISK_SNAPSHOTS = "CREATE_REPLICA_DISK_SNAPSHOTS"
TASK_TYPE_DELETE_REPLICA_DISK_SNAPSHOTS = "DELETE_REPLICA_DISK_SNAPSHOTS"
TASK_TYPE_RESTORE_REPLICA_DISK_SNAPSHOTS = "RESTORE_REPLICA_DISK_SNAPSHOTS"
TASK_TYPE_GET_OPTIMAL_FLAVOR = "GET_OPTIMAL_FLAVOR"
TASK_TYPE_VALIDATE_MIGRATION_SOURCE_INPUTS = (
    "VALIDATE_MIGRATION_SOURCE_INPUTS")
TASK_TYPE_VALIDATE_MIGRATION_DESTINATION_INPUTS = (
    "VALIDATE_MIGRATION_DESTINATION_INPUTS")
TASK_TYPE_VALIDATE_REPLICA_SOURCE_INPUTS = "VALIDATE_REPLICA_SOURCE_INPUTS"
TASK_TYPE_VALIDATE_REPLICA_DESTINATION_INPUTS = (
    "VALIDATE_REPLICA_DESTINATION_INPUTS")
TASK_TYPE_VALIDATE_REPLICA_DEPLOYMENT_INPUTS = (
    "VALIDATE_REPLICA_DEPLOYMENT_INPUTS")
TASK_TYPE_UPDATE_SOURCE_REPLICA = "UPDATE_SOURCE_REPLICA"
TASK_TYPE_UPDATE_DESTINATION_REPLICA = "UPDATE_DESTINATION_REPLICA"

PROVIDER_TYPE_IMPORT = 1
PROVIDER_TYPE_EXPORT = 2
PROVIDER_TYPE_REPLICA_IMPORT = 4
PROVIDER_TYPE_REPLICA_EXPORT = 8
PROVIDER_TYPE_ENDPOINT = 16
PROVIDER_TYPE_ENDPOINT_INSTANCES = 32
PROVIDER_TYPE_OS_MORPHING = 64
PROVIDER_TYPE_ENDPOINT_NETWORKS = 128
PROVIDER_TYPE_INSTANCE_FLAVOR = 256
PROVIDER_TYPE_DESTINATION_ENDPOINT_OPTIONS = 512
PROVIDER_TYPE_SETUP_LIBS = 1024
PROVIDER_TYPE_VALIDATE_MIGRATION_EXPORT = 2048
PROVIDER_TYPE_VALIDATE_REPLICA_EXPORT = 4096
PROVIDER_TYPE_VALIDATE_MIGRATION_IMPORT = 8192
PROVIDER_TYPE_VALIDATE_REPLICA_IMPORT = 16384
PROVIDER_TYPE_ENDPOINT_STORAGE = 32768
PROVIDER_TYPE_SOURCE_REPLICA_UPDATE = 65536
PROVIDER_TYPE_SOURCE_ENDPOINT_OPTIONS = 131072
PROVIDER_TYPE_DESTINATION_REPLICA_UPDATE = 262144

DISK_FORMAT_VMDK = 'vmdk'
DISK_FORMAT_RAW = 'raw'
DISK_FORMAT_QCOW = "qcow"
DISK_FORMAT_QCOW2 = 'qcow2'
DISK_FORMAT_VHD = 'vhd'
DISK_FORMAT_VHDX = 'vhdx'

DISK_ALLOCATION_TYPE_STATIC = "static"
DISK_ALLOCATION_TYPE_DYNAMIC = "dynamic"

FIRMWARE_TYPE_BIOS = 'BIOS'
FIRMWARE_TYPE_EFI = 'EFI'

HYPERVISOR_VMWARE = "vmware"
HYPERVISOR_HYPERV = "hyperv"
HYPERVISOR_QEMU = "qemu"
HYPERVISOR_KVM = "kvm"
HYPERVISOR_XENSERVER = "xenserver"

TASK_EVENT_INFO = "INFO"
TASK_EVENT_WARNING = "WARNING"
TASK_EVENT_ERROR = "ERROR"

OS_TYPE_BSD = "bsd"
OS_TYPE_LINUX = "linux"
OS_TYPE_OS_X = "osx"
OS_TYPE_SOLARIS = "solaris"
OS_TYPE_WINDOWS = "windows"
OS_TYPE_OTHER = "other"
OS_TYPE_UNKNOWN = "unknown"

DEFAULT_OS_TYPE = OS_TYPE_LINUX

TMP_DIRS_KEY = "__tmp_dirs"

COMPRESSION_FORMAT_GZIP = "gzip"
COMPRESSION_FORMAT_ZLIB = "zlib"

VALID_COMPRESSION_FORMATS = [
    COMPRESSION_FORMAT_GZIP,
    COMPRESSION_FORMAT_ZLIB
]

EXECUTION_TYPE_REPLICA_EXECUTION = "replica_execution"
EXECUTION_TYPE_REPLICA_DISKS_DELETE = "replica_disks_delete"
EXECUTION_TYPE_REPLICA_DEPLOY = "replica_deploy"
EXECUTION_TYPE_MIGRATION = "migration"
EXECUTION_TYPE_REPLICA_UPDATE = "replica_update"
