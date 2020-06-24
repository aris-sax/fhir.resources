# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Device
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Device(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item used in healthcare.
    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """

    resource_type = Field("Device", const=True)

    contact: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="Details for human/organization for support",
        description=(
            "Contact details for an organization or a particular human that is "
            "responsible for the device."
        ),
    )

    definition: fhirtypes.ReferenceType = Field(
        None,
        alias="definition",
        title="The reference to the definition for the device",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["DeviceDefinition"],
    )

    deviceName: ListType[fhirtypes.DeviceDeviceNameType] = Field(
        None,
        alias="deviceName",
        title="The name of the device as given by the manufacturer",
        description=(
            "This represents the manufacturer's name of the device as provided by "
            "the device, from a UDI label, or by a person describing the Device.  "
            "This typically would be used when a person provides the name(s) or "
            "when the device represents one of the names available from "
            "DeviceDefinition."
        ),
    )

    distinctIdentifier: fhirtypes.String = Field(
        None,
        alias="distinctIdentifier",
        title="The distinct identification string",
        description=(
            "The distinct identification string as required by regulation for a "
            "human cell, tissue, or cellular and tissue-based product."
        ),
    )
    distinctIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_distinctIdentifier",
        title="Extension field for ``distinctIdentifier``.",
    )

    expirationDate: fhirtypes.DateTime = Field(
        None,
        alias="expirationDate",
        title="Date and time of expiry of this device (if applicable)",
        description=(
            "The date and time beyond which this device is no longer valid or "
            "should not be used (if applicable)."
        ),
    )
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expirationDate", title="Extension field for ``expirationDate``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Instance identifier",
        description=(
            "Unique instance identifiers assigned to a device by manufacturers "
            "other organizations or owners."
        ),
    )

    location: fhirtypes.ReferenceType = Field(
        None,
        alias="location",
        title="Where the device is found",
        description="The place where the device can be found.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Location"],
    )

    lotNumber: fhirtypes.String = Field(
        None,
        alias="lotNumber",
        title="Lot number of manufacture",
        description="Lot number assigned by the manufacturer.",
    )
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lotNumber", title="Extension field for ``lotNumber``."
    )

    manufactureDate: fhirtypes.DateTime = Field(
        None,
        alias="manufactureDate",
        title="Date when the device was made",
        description="The date and time when the device was manufactured.",
    )
    manufactureDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_manufactureDate", title="Extension field for ``manufactureDate``."
    )

    manufacturer: fhirtypes.String = Field(
        None,
        alias="manufacturer",
        title="Name of device manufacturer",
        description="A name of the manufacturer.",
    )
    manufacturer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_manufacturer", title="Extension field for ``manufacturer``."
    )

    modelNumber: fhirtypes.String = Field(
        None,
        alias="modelNumber",
        title="The model number for the device",
        description=None,
    )
    modelNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_modelNumber", title="Extension field for ``modelNumber``."
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Device notes and comments",
        description=(
            "Descriptive information, usage information or implantation information"
            " that is not captured in an existing element."
        ),
    )

    owner: fhirtypes.ReferenceType = Field(
        None,
        alias="owner",
        title="Organization responsible for device",
        description=(
            "An organization that is responsible for the provision and ongoing "
            "maintenance of the device."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    parent: fhirtypes.ReferenceType = Field(
        None,
        alias="parent",
        title="The parent device",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Device"],
    )

    partNumber: fhirtypes.String = Field(
        None,
        alias="partNumber",
        title="The part number of the device",
        description=None,
    )
    partNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_partNumber", title="Extension field for ``partNumber``."
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Patient to whom Device is affixed",
        description="Patient information, If the device is affixed to a person.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    property: ListType[fhirtypes.DevicePropertyType] = Field(
        None,
        alias="property",
        title=(
            "The actual configuration settings of a device as it actually operates,"
            " e.g., regulation status, time properties"
        ),
        description=None,
    )

    safety: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="safety",
        title="Safety Characteristics of Device",
        description=(
            "Provides additional safety characteristics about a medical device.  "
            "For example devices containing latex."
        ),
    )

    serialNumber: fhirtypes.String = Field(
        None,
        alias="serialNumber",
        title="Serial number assigned by the manufacturer",
        description=(
            "The serial number assigned by the organization when the device was "
            "manufactured."
        ),
    )
    serialNumber__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_serialNumber", title="Extension field for ``serialNumber``."
    )

    specialization: ListType[fhirtypes.DeviceSpecializationType] = Field(
        None,
        alias="specialization",
        title=(
            "The capabilities supported on a  device, the standards to which the "
            "device conforms for a particular purpose, and used for the "
            "communication"
        ),
        description=None,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | inactive | entered-in-error | unknown",
        description="Status of the Device availability.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "inactive", "entered-in-error", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    statusReason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="statusReason",
        title=(
            "online | paused | standby | offline | not-ready | transduc-discon | "
            "hw-discon | off"
        ),
        description="Reason for the dtatus of the Device availability.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None, alias="type", title="The kind or type of device", description=None,
    )

    udiCarrier: ListType[fhirtypes.DeviceUdiCarrierType] = Field(
        None,
        alias="udiCarrier",
        title="Unique Device Identifier (UDI) Barcode string",
        description=(
            "Unique device identifier (UDI) assigned to device label or package.  "
            "Note that the Device may include multiple udiCarriers as it either may"
            " include just the udiCarrier for the jurisdiction it is sold, or for "
            "multiple jurisdictions it could have been sold."
        ),
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Network address to contact device",
        description="A network address on which the device may be contacted directly.",
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    version: ListType[fhirtypes.DeviceVersionType] = Field(
        None,
        alias="version",
        title=(
            "The actual design of the device or software version running on the "
            "device"
        ),
        description=None,
    )


class DeviceDeviceName(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The name of the device as given by the manufacturer.
    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """

    resource_type = Field("DeviceDeviceName", const=True)

    name: fhirtypes.String = Field(
        ..., alias="name", title="The name of the device", description=None,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title=(
            "udi-label-name | user-friendly-name | patient-reported-name | "
            "manufacturer-name | model-name | other"
        ),
        description=(
            "The type of deviceName. UDILabelName | UserFriendlyName | "
            "PatientReportedName | ManufactureDeviceName | ModelName."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "udi-label-name",
            "user-friendly-name",
            "patient-reported-name",
            "manufacturer-name",
            "model-name",
            "other",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class DeviceProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """

    resource_type = Field("DeviceProperty", const=True)

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title=(
            "Code that specifies the property DeviceDefinitionPropetyCode "
            "(Extensible)"
        ),
        description=None,
    )

    valueCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="valueCode",
        title="Property value as a code, e.g., NTP4 (synced to NTP)",
        description=None,
    )

    valueQuantity: ListType[fhirtypes.QuantityType] = Field(
        None,
        alias="valueQuantity",
        title="Property value as a quantity",
        description=None,
    )


class DeviceSpecialization(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """

    resource_type = Field("DeviceSpecialization", const=True)

    systemType: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="systemType",
        title="The standard that is used to operate and communicate",
        description=None,
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="The version of the standard that is used to operate and communicate",
        description=None,
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class DeviceUdiCarrier(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Unique Device Identifier (UDI) Barcode string.
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """

    resource_type = Field("DeviceUdiCarrier", const=True)

    carrierAIDC: fhirtypes.Base64Binary = Field(
        None,
        alias="carrierAIDC",
        title="UDI Machine Readable Barcode String",
        description=(
            "The full UDI carrier of the Automatic Identification and Data Capture "
            "(AIDC) technology representation of the barcode string as printed on "
            "the packaging of the device - e.g., a barcode or RFID.   Because of "
            "limitations on character sets in XML and the need to round-trip JSON "
            "data through XML, AIDC Formats *SHALL* be base64 encoded."
        ),
    )
    carrierAIDC__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_carrierAIDC", title="Extension field for ``carrierAIDC``."
    )

    carrierHRF: fhirtypes.String = Field(
        None,
        alias="carrierHRF",
        title="UDI Human Readable Barcode String",
        description=(
            "The full UDI carrier as the human readable form (HRF) representation "
            "of the barcode string as printed on the packaging of the device."
        ),
    )
    carrierHRF__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_carrierHRF", title="Extension field for ``carrierHRF``."
    )

    deviceIdentifier: fhirtypes.String = Field(
        None,
        alias="deviceIdentifier",
        title="Mandatory fixed portion of UDI",
        description=(
            "The device identifier (DI) is a mandatory, fixed portion of a UDI that"
            " identifies the labeler and the specific version or model of a device."
        ),
    )
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_deviceIdentifier",
        title="Extension field for ``deviceIdentifier``.",
    )

    entryType: fhirtypes.Code = Field(
        None,
        alias="entryType",
        title="barcode | rfid | manual +",
        description="A coded entry to indicate how the data was entered.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["barcode", "rfid", "manual +"],
    )
    entryType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_entryType", title="Extension field for ``entryType``."
    )

    issuer: fhirtypes.Uri = Field(
        None,
        alias="issuer",
        title="UDI Issuing Organization",
        description=(
            "Organization that is charged with issuing UDIs for devices.  For "
            "example, the US FDA issuers include : 1) GS1:  "
            "http://hl7.org/fhir/NamingSystem/gs1-di,  2) HIBCC: "
            "http://hl7.org/fhir/NamingSystem/hibcc-dI,  3) ICCBBA for blood "
            "containers: http://hl7.org/fhir/NamingSystem/iccbba-blood-di,  4) "
            "ICCBA for other devices: http://hl7.org/fhir/NamingSystem/iccbba-"
            "other-di."
        ),
    )
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_issuer", title="Extension field for ``issuer``."
    )

    jurisdiction: fhirtypes.Uri = Field(
        None,
        alias="jurisdiction",
        title="Regional UDI authority",
        description=(
            "The identity of the authoritative source for UDI generation within a  "
            "jurisdiction.  All UDIs are globally unique within a single namespace "
            "with the appropriate repository uri as the system.  For example,  UDIs"
            " of devices managed in the U.S. by the FDA, the value is  "
            "http://hl7.org/fhir/NamingSystem/fda-udi."
        ),
    )
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_jurisdiction", title="Extension field for ``jurisdiction``."
    )


class DeviceVersion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The actual design of the device or software version running on the device.
    """

    resource_type = Field("DeviceVersion", const=True)

    component: fhirtypes.IdentifierType = Field(
        None,
        alias="component",
        title="A single component of the device version",
        description=None,
    )

    type: fhirtypes.CodeableConceptType = Field(
        None, alias="type", title="The type of the device version", description=None,
    )

    value: fhirtypes.String = Field(
        ..., alias="value", title="The version text", description=None,
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )
