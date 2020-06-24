# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NamingSystem
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class NamingSystem(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    System of unique identification.
    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """

    resource_type = Field("NamingSystem", const=True)

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the naming system was published. "
            "The date must change when the business version changes and it must "
            "change if the status code changes. In addition, it should change when "
            "the substantive content of the naming system changes."
        ),
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the naming system",
        description=(
            "A free text natural language description of the naming system from a "
            "consumer's perspective. Details about what the namespace identifies "
            "including scope, granularity, version labeling, etc."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for naming system (if applicable)",
        description=(
            "A legal or geographic region in which the naming system is intended to"
            " be used."
        ),
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="codesystem | identifier | root",
        description=(
            "Indicates the purpose for the naming system - what kinds of things "
            "does it make unique?"
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["codesystem", "identifier", "root"],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name for this naming system (computer friendly)",
        description=(
            "A natural language name identifying the naming system. This name "
            "should be usable as an identifier for the module by machine processing"
            " applications such as code generation."
        ),
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the naming "
            "system."
        ),
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    responsible: fhirtypes.String = Field(
        None,
        alias="responsible",
        title="Who maintains system namespace?",
        description=(
            "The name of the organization that is responsible for issuing "
            "identifiers or codes for this namespace and ensuring their non-"
            "collision."
        ),
    )
    responsible__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_responsible", title="Extension field for ``responsible``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this naming system. Enables tracking the life-cycle of "
            "the content."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="e.g. driver,  provider,  patient, bank etc.",
        description=(
            "Categorizes a naming system for easier search by grouping related "
            "naming systems."
        ),
    )

    uniqueId: ListType[fhirtypes.NamingSystemUniqueIdType] = Field(
        ...,
        alias="uniqueId",
        title="Unique identifiers used for system",
        description=(
            "Indicates how the system may be identified when referenced in "
            "electronic exchange."
        ),
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="How/where is it used",
        description=(
            "Provides guidance on the use of the namespace, including the handling "
            "of formatting characters, use of upper vs. lower case, etc."
        ),
    )
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_usage", title="Extension field for ``usage``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate naming system instances."
        ),
    )


class NamingSystemUniqueId(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Unique identifiers used for system.
    Indicates how the system may be identified when referenced in electronic
    exchange.
    """

    resource_type = Field("NamingSystemUniqueId", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Notes about identifier usage",
        description="Notes about the past or intended usage of this identifier.",
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="When is identifier valid?",
        description=(
            "Identifies the period of time over which this identifier is considered"
            " appropriate to refer to the naming system.  Outside of this window, "
            "the identifier might be non-deterministic."
        ),
    )

    preferred: bool = Field(
        None,
        alias="preferred",
        title="Is this the id that should be used for this type",
        description=(
            'Indicates whether this identifier is the "preferred" identifier of '
            "this type."
        ),
    )
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preferred", title="Extension field for ``preferred``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="oid | uuid | uri | other",
        description=(
            "Identifies the unique identifier scheme used for this particular "
            "identifier."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["oid", "uuid", "uri", "other"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="The unique identifier",
        description=(
            "The string that should be sent over the wire to identify the code "
            "system or identifier system."
        ),
    )
    value__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_value", title="Extension field for ``value``."
    )
