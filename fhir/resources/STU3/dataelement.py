# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DataElement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class DataElement(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource data element.
    The formal description of a single piece of information that can be
    gathered and reported.
    """

    resource_type = Field("DataElement", const=True)

    contact: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
    )

    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the data element and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the data element."
        ),
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the data element was published. "
            "The date must change if and when the business version changes and it "
            "must change if the status code changes. In addition, it should change "
            "when the substantive content of the data element changes."
        ),
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    element: ListType[fhirtypes.ElementDefinitionType] = Field(
        ...,
        alias="element",
        title="Definition of element",
        description=(
            "Defines the structure, type, allowed values and other constraining "
            "characteristics of the data element."
        ),
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this data element is authored for "
            "testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the data element",
        description=(
            "A formal identifier that is used to identify this data element when it"
            " is represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for data element (if applicable)",
        description=(
            "A legal or geographic region in which the data element is intended to "
            "be used."
        ),
    )

    mapping: ListType[fhirtypes.DataElementMappingType] = Field(
        None,
        alias="mapping",
        title="External specification mapped to",
        description=(
            "Identifies a specification (other than a terminology) that the "
            "elements which make up the DataElement have some correspondence with."
        ),
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this data element (computer friendly)",
        description=(
            "A natural language name identifying the data element. This name should"
            " be usable as an identifier for the module by machine processing "
            "applications such as code generation."
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
            "The name of the individual or organization that published the data "
            "element."
        ),
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this data element. Enables tracking the life-cycle of "
            "the content."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    stringency: fhirtypes.Code = Field(
        None,
        alias="stringency",
        title=(
            "comparable | fully-specified | equivalent | convertable | scaleable | "
            "flexible"
        ),
        description="Identifies how precise the data element is in its definition.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "comparable",
            "fully-specified",
            "equivalent",
            "convertable",
            "scaleable",
            "flexible",
        ],
    )
    stringency__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_stringency", title="Extension field for ``stringency``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this data element (human friendly)",
        description="A short, descriptive, user-friendly title for the data element.",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URI to reference this data element (globally unique)",
        description=(
            "An absolute URI that is used to identify this data element when it is "
            "referenced in a specification, model, design or an instance. This "
            "SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at"
            " which this data element is (or will be) published. The URL SHOULD "
            "include the major version of the data element. For more information "
            "see [Technical and Business Versions](resource.html#versions)."
        ),
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: ListType[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="Context the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These terms may be used to assist with "
            "indexing and searching for appropriate data element instances."
        ),
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the data element",
        description=(
            "The identifier that is used to identify this version of the data "
            "element when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the data element "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence."
        ),
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class DataElementMapping(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    External specification mapped to.
    Identifies a specification (other than a terminology) that the elements
    which make up the DataElement have some correspondence with.
    """

    resource_type = Field("DataElementMapping", const=True)

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title="Versions, issues, scope limitations, etc.",
        description=(
            "Comments about this mapping, including version notes, issues, scope "
            "limitations, and other important notes for usage."
        ),
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identity: fhirtypes.Id = Field(
        ...,
        alias="identity",
        title="Internal id when this mapping is used",
        description=(
            "An internal id that is used to identify this mapping set when specific"
            " mappings are made on a per-element basis."
        ),
    )
    identity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_identity", title="Extension field for ``identity``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Names what this mapping refers to",
        description="A name for the specification that is being mapped to.",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    uri: fhirtypes.Uri = Field(
        None,
        alias="uri",
        title="Identifies what this mapping refers to",
        description=(
            "An absolute URI that identifies the specification that this mapping is"
            " expressed to."
        ),
    )
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uri", title="Extension field for ``uri``."
    )
