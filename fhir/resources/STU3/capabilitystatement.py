# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType
from typing import Union

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CapabilityStatement(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A statement of system capabilities.
    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server functionality
    or a statement of required or desired server implementation.
    """

    resource_type = Field("CapabilityStatement", const=True)

    acceptUnknown: fhirtypes.Code = Field(
        ...,
        alias="acceptUnknown",
        title="no | extensions | elements | both",
        description=(
            "A code that indicates whether the application accepts unknown elements"
            " or extensions when reading resources."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["no", "extensions", "elements", "both"],
    )
    acceptUnknown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_acceptUnknown", title="Extension field for ``acceptUnknown``."
    )

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
            "A copyright statement relating to the capability statement and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the capability statement."
        ),
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        ...,
        alias="date",
        title="Date this was last changed",
        description=(
            "The date  (and optionally time) when the capability statement was "
            "published. The date must change if and when the business version "
            "changes and it must change if the status code changes. In addition, it"
            " should change when the substantive content of the capability "
            "statement changes."
        ),
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the capability statement",
        description=(
            "A free text natural language description of the capability statement "
            "from a consumer's perspective. Typically, this is used when the "
            "capability statement describes a desired rather than an actual "
            "solution, for example as a formal expression of requirements as part "
            "of an RFP."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    document: ListType[fhirtypes.CapabilityStatementDocumentType] = Field(
        None,
        alias="document",
        title="Document definition",
        description="A document definition.",
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A boolean value to indicate that this capability statement is authored"
            " for testing purposes (or education/evaluation/marketing), and is not "
            "intended to be used for genuine usage."
        ),
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    fhirVersion: fhirtypes.Id = Field(
        ...,
        alias="fhirVersion",
        title="FHIR Version the system uses",
        description=(
            "The version of the FHIR specification on which this capability "
            "statement is based."
        ),
    )
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_fhirVersion", title="Extension field for ``fhirVersion``."
    )

    format: ListType[fhirtypes.Code] = Field(
        ...,
        alias="format",
        title="formats supported (xml | json | ttl | mime type)",
        description=(
            "A list of the formats supported by this implementation using their "
            "content types."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["formats supported (xml", "json", "ttl", "mime type)"],
    )
    format__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_format", title="Extension field for ``format``."
    )

    implementation: fhirtypes.CapabilityStatementImplementationType = Field(
        None,
        alias="implementation",
        title="If this describes a specific instance",
        description=(
            "Identifies a specific implementation instance that is described by the"
            " capability statement - i.e. a particular installation, rather than "
            "the capabilities of a software program."
        ),
    )

    implementationGuide: ListType[fhirtypes.Uri] = Field(
        None,
        alias="implementationGuide",
        title="Implementation guides supported",
        description=(
            "A list of implementation guides that the server does (or should) "
            "support in their entirety."
        ),
    )
    implementationGuide__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_implementationGuide",
        title="Extension field for ``implementationGuide``.",
    )

    instantiates: ListType[fhirtypes.Uri] = Field(
        None,
        alias="instantiates",
        title="Canonical URL of another capability statement this implements",
        description=(
            "Reference to a canonical URL of another CapabilityStatement that this "
            "software implements or uses. This capability statement is a published "
            "API description that corresponds to a business service. The rest of "
            "the capability statement does not need to repeat the details of the "
            "referenced resource, but can do so."
        ),
    )
    instantiates__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_instantiates", title="Extension field for ``instantiates``."
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for capability statement (if applicable)",
        description=(
            "A legal or geographic region in which the capability statement is "
            "intended to be used."
        ),
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="instance | capability | requirements",
        description=(
            "The way that this statement is intended to be used, to describe an "
            "actual running instance of software, a particular product (kind not "
            "instance of software) or a class of implementation (e.g. a desired "
            "purchase)."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["instance", "capability", "requirements"],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )

    messaging: ListType[fhirtypes.CapabilityStatementMessagingType] = Field(
        None,
        alias="messaging",
        title="If messaging is supported",
        description="A description of the messaging capabilities of the solution.",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this capability statement (computer friendly)",
        description=(
            "A natural language name identifying the capability statement. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    patchFormat: ListType[fhirtypes.Code] = Field(
        None,
        alias="patchFormat",
        title="Patch formats supported",
        description=(
            "A list of the patch formats supported by this implementation using "
            "their content types."
        ),
    )
    patchFormat__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_patchFormat", title="Extension field for ``patchFormat``.")

    profile: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="profile",
        title="Profiles for use cases supported",
        description=(
            "A list of profiles that represent different use cases supported by the"
            ' system. For a server, "supported by the system" means the system '
            "hosts/produces a set of resources that are conformant to a particular "
            "profile, and allows clients that use its services to search using this"
            " profile and to find appropriate data. For a client, it means the "
            "system will search by this profile and process data according to the "
            "guidance implicit in the profile. See further discussion in [Using "
            "Profiles](profiling.html#profile-uses)."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )

    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the individual or organization that published the "
            "capability statement."
        ),
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this capability statement is defined",
        description=(
            "Explaination of why this capability statement is needed and why it has"
            " been designed as it has."
        ),
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    rest: ListType[fhirtypes.CapabilityStatementRestType] = Field(
        None,
        alias="rest",
        title="If the endpoint is a RESTful one",
        description="A definition of the restful capabilities of the solution, if any.",
    )

    software: fhirtypes.CapabilityStatementSoftwareType = Field(
        None,
        alias="software",
        title="Software that is covered by this capability statement",
        description=(
            "Software that is covered by this capability statement.  It is used "
            "when the capability statement describes the capabilities of a "
            "particular software version, independent of an installation."
        ),
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this capability statement. Enables tracking the life-"
            "cycle of the content."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this capability statement (human friendly)",
        description=(
            "A short, descriptive, user-friendly title for the capability " "statement."
        ),
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Logical URI to reference this capability statement (globally unique)",
        description=(
            "An absolute URI that is used to identify this capability statement "
            "when it is referenced in a specification, model, design or an "
            "instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD "
            "be an address at which this capability statement is (or will be) "
            "published. The URL SHOULD include the major version of the capability "
            "statement. For more information see [Technical and Business "
            "Versions](resource.html#versions)."
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
            "indexing and searching for appropriate capability statement instances."
        ),
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the capability statement",
        description=(
            "The identifier that is used to identify this version of the capability"
            " statement when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the capability "
            "statement author and is not expected to be globally unique. For "
            "example, it might be a timestamp (e.g. yyyymmdd) if a managed version "
            "is not available. There is also no expectation that versions can be "
            "placed in a lexicographical sequence."
        ),
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )


class CapabilityStatementDocument(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Document definition.
    A document definition.
    """

    resource_type = Field("CapabilityStatementDocument", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Description of document support",
        description=(
            "A description of how the application supports or uses the specified "
            "document profile.  For example, when documents are created, what "
            "action is taken with consumed documents, etc."
        ),
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="producer | consumer",
        description=(
            "Mode of this document declaration - whether an application is a "
            "producer or consumer."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["producer", "consumer"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    profile: fhirtypes.ReferenceType = Field(
        ...,
        alias="profile",
        title="Constraint on a resource used in the document",
        description="A constraint on a resource used in the document.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )


class CapabilityStatementImplementation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this describes a specific instance.
    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """

    resource_type = Field("CapabilityStatementImplementation", const=True)

    description: fhirtypes.String = Field(
        ...,
        alias="description",
        title="Describes this specific instance",
        description=(
            "Information about the specific installation that this capability "
            "statement relates to."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title="Base URL for the installation",
        description=(
            "An absolute base URL for the implementation.  This forms the base for "
            "REST interfaces as well as the mailbox and document interfaces."
        ),
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )


class CapabilityStatementMessaging(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If messaging is supported.
    A description of the messaging capabilities of the solution.
    """

    resource_type = Field("CapabilityStatementMessaging", const=True)

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Messaging interface behavior details",
        description=(
            "Documentation about the system's messaging capabilities for this "
            "endpoint not otherwise documented by the capability statement.  For "
            "example, the process for becoming an authorized messaging exchange "
            "partner."
        ),
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    endpoint: ListType[fhirtypes.CapabilityStatementMessagingEndpointType] = Field(
        None,
        alias="endpoint",
        title="Where messages should be sent",
        description=(
            "An endpoint (network accessible address) to which messages and/or "
            "replies are to be sent."
        ),
    )

    event: ListType[fhirtypes.CapabilityStatementMessagingEventType] = Field(
        None,
        alias="event",
        title="Declare support for this event",
        description=(
            "A description of the solution's support for an event at this end-" "point."
        ),
    )

    reliableCache: fhirtypes.UnsignedInt = Field(
        None,
        alias="reliableCache",
        title="Reliable Message Cache Length (min)",
        description=(
            "Length if the receiver's reliable messaging cache in minutes (if a "
            "receiver) or how long the cache length on the receiver should be (if a"
            " sender)."
        ),
    )
    reliableCache__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reliableCache", title="Extension field for ``reliableCache``."
    )

    supportedMessage: ListType[
        fhirtypes.CapabilityStatementMessagingSupportedMessageType
    ] = Field(
        None,
        alias="supportedMessage",
        title="Messages supported by this system",
        description=(
            "References to message definitions for messages this system can send or"
            " receive."
        ),
    )


class CapabilityStatementMessagingEndpoint(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Where messages should be sent.
    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """

    resource_type = Field("CapabilityStatementMessagingEndpoint", const=True)

    address: fhirtypes.Uri = Field(
        ...,
        alias="address",
        title="Network address or identifier of the end-point",
        description=(
            "The network address of the end-point. For solutions that do not use "
            "network addresses for routing, it can be just an identifier."
        ),
    )
    address__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_address", title="Extension field for ``address``."
    )

    protocol: fhirtypes.CodingType = Field(
        ...,
        alias="protocol",
        title="http | ftp | mllp +",
        description=(
            "A list of the messaging transport protocol(s) identifiers, supported "
            "by this endpoint."
        ),
    )


class CapabilityStatementMessagingEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Declare support for this event.
    A description of the solution's support for an event at this end-point.
    """

    resource_type = Field("CapabilityStatementMessagingEvent", const=True)

    category: fhirtypes.Code = Field(
        None,
        alias="category",
        title="Consequence | Currency | Notification",
        description="The impact of the content of the message.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["Consequence", "Currency", "Notification"],
    )
    category__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_category", title="Extension field for ``category``."
    )

    code: fhirtypes.CodingType = Field(
        ...,
        alias="code",
        title="Event type",
        description="A coded identifier of a supported messaging event.",
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Endpoint-specific event documentation",
        description=(
            "Guidance on how this event is handled, such as internal system trigger"
            " points, business rules, etc."
        ),
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    focus: fhirtypes.Code = Field(
        ...,
        alias="focus",
        title="Resource that's focus of message",
        description=(
            "A resource associated with the event.  This is the resource that "
            "defines the event."
        ),
    )
    focus__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_focus", title="Extension field for ``focus``."
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="sender | receiver",
        description=(
            "The mode of this event declaration - whether an application is a "
            "sender or receiver."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["sender", "receiver"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    request: fhirtypes.ReferenceType = Field(
        ...,
        alias="request",
        title="Profile that describes the request",
        description="Information about the request for this event.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )

    response: fhirtypes.ReferenceType = Field(
        ...,
        alias="response",
        title="Profile that describes the response",
        description="Information about the response for this event.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )


class CapabilityStatementMessagingSupportedMessage(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Messages supported by this system.
    References to message definitions for messages this system can send or
    receive.
    """

    resource_type = Field("CapabilityStatementMessagingSupportedMessage", const=True)

    definition: fhirtypes.ReferenceType = Field(
        ...,
        alias="definition",
        title="Message supported by this system",
        description=(
            "Points to a message definition that identifies the messaging event, "
            "message structure, allowed responses, etc."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MessageDefinition"],
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="sender | receiver",
        description=(
            "The mode of this event declaration - whether application is sender or "
            "receiver."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["sender", "receiver"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )


class CapabilityStatementRest(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If the endpoint is a RESTful one.
    A definition of the restful capabilities of the solution, if any.
    """

    resource_type = Field("CapabilityStatementRest", const=True)

    compartment: ListType[fhirtypes.Uri] = Field(
        None,
        alias="compartment",
        title="Compartments served/used by system",
        description=(
            "An absolute URI which is a reference to the definition of a "
            "compartment that the system supports. The reference is to a "
            "CompartmentDefinition resource by its canonical URL ."
        ),
    )
    compartment__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_compartment", title="Extension field for ``compartment``.")

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="General description of implementation",
        description=(
            "Information about the system's restful capabilities that apply across "
            "all applications, such as security."
        ),
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    interaction: ListType[fhirtypes.CapabilityStatementRestInteractionType] = Field(
        None,
        alias="interaction",
        title="What operations are supported?",
        description="A specification of restful operations supported by the system.",
    )

    mode: fhirtypes.Code = Field(
        ...,
        alias="mode",
        title="client | server",
        description=(
            "Identifies whether this portion of the statement is describing the "
            "ability to initiate or receive restful operations."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["client", "server"],
    )
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_mode", title="Extension field for ``mode``."
    )

    operation: ListType[fhirtypes.CapabilityStatementRestOperationType] = Field(
        None,
        alias="operation",
        title="Definition of an operation or a custom query",
        description=(
            "Definition of an operation or a named query together with its "
            "parameters and their meaning and type."
        ),
    )

    resource: ListType[fhirtypes.CapabilityStatementRestResourceType] = Field(
        None,
        alias="resource",
        title="Resource served on the REST interface",
        description=(
            "A specification of the restful capabilities of the solution for a "
            "specific resource type."
        ),
    )

    searchParam: ListType[
        fhirtypes.CapabilityStatementRestResourceSearchParamType
    ] = Field(
        None,
        alias="searchParam",
        title="Search parameters for searching all resources",
        description=(
            "Search parameters that are supported for searching all resources for "
            "implementations to support and/or make use of - either references to "
            "ones defined in the specification, or additional ones defined for/by "
            "the implementation."
        ),
    )

    security: fhirtypes.CapabilityStatementRestSecurityType = Field(
        None,
        alias="security",
        title="Information about security of implementation",
        description=(
            "Information about security implementation from an interface "
            "perspective - what a client needs to know."
        ),
    )


class CapabilityStatementRestInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What operations are supported?.
    A specification of restful operations supported by the system.
    """

    resource_type = Field("CapabilityStatementRestInteraction", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title="transaction | batch | search-system | history-system",
        description="A coded identifier of the operation, supported by the system.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["transaction", "batch", "search-system", "history-system"],
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Anything special about operation behavior",
        description=(
            "Guidance specific to the implementation of this operation, such as "
            "limitations on the kind of transactions allowed, or information about "
            "system wide search is implemented."
        ),
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )


class CapabilityStatementRestOperation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Definition of an operation or a custom query.
    Definition of an operation or a named query together with its parameters
    and their meaning and type.
    """

    resource_type = Field("CapabilityStatementRestOperation", const=True)

    definition: fhirtypes.ReferenceType = Field(
        ...,
        alias="definition",
        title="The defined operation/query",
        description="Where the formal definition can be found.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["OperationDefinition"],
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name by which the operation/query is invoked",
        description=(
            "The name of the operation or query. For an operation, this is the name"
            "  prefixed with $ and used in the URL. For a query, this is the name "
            "used in the _query parameter when the query is called."
        ),
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )


class CapabilityStatementRestResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Resource served on the REST interface.
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """

    resource_type = Field("CapabilityStatementRestResource", const=True)

    conditionalCreate: bool = Field(
        None,
        alias="conditionalCreate",
        title="If allows/uses conditional create",
        description="A flag that indicates that the server supports conditional create.",
    )
    conditionalCreate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_conditionalCreate",
        title="Extension field for ``conditionalCreate``.",
    )

    conditionalDelete: fhirtypes.Code = Field(
        None,
        alias="conditionalDelete",
        title=(
            "not-supported | single | multiple - how conditional delete is " "supported"
        ),
        description="A code that indicates how the server supports conditional delete.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "not-supported",
            "single",
            "multiple - how conditional delete is supported",
        ],
    )
    conditionalDelete__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_conditionalDelete",
        title="Extension field for ``conditionalDelete``.",
    )

    conditionalRead: fhirtypes.Code = Field(
        None,
        alias="conditionalRead",
        title="not-supported | modified-since | not-match | full-support",
        description="A code that indicates how the server supports conditional read.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["not-supported", "modified-since", "not-match", "full-support"],
    )
    conditionalRead__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_conditionalRead", title="Extension field for ``conditionalRead``."
    )

    conditionalUpdate: bool = Field(
        None,
        alias="conditionalUpdate",
        title="If allows/uses conditional update",
        description="A flag that indicates that the server supports conditional update.",
    )
    conditionalUpdate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_conditionalUpdate",
        title="Extension field for ``conditionalUpdate``.",
    )

    documentation: fhirtypes.Markdown = Field(
        None,
        alias="documentation",
        title="Additional information about the use of the resource type",
        description="Additional information about the resource type used by the system.",
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    interaction: ListType[
        fhirtypes.CapabilityStatementRestResourceInteractionType
    ] = Field(
        ...,
        alias="interaction",
        title="What operations are supported?",
        description="Identifies a restful operation supported by the solution.",
    )

    profile: fhirtypes.ReferenceType = Field(
        None,
        alias="profile",
        title="Base System profile for all uses of resource",
        description=(
            "A specification of the profile that describes the solution's overall "
            "support for the resource, including any constraints on cardinality, "
            "bindings, lengths or other limitations. See further discussion in "
            "[Using Profiles](profiling.html#profile-uses)."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureDefinition"],
    )

    readHistory: bool = Field(
        None,
        alias="readHistory",
        title="Whether vRead can return past versions",
        description=(
            "A flag for whether the server is able to return past versions as part "
            "of the vRead operation."
        ),
    )
    readHistory__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_readHistory", title="Extension field for ``readHistory``."
    )

    referencePolicy: ListType[fhirtypes.Code] = Field(
        None,
        alias="referencePolicy",
        title="literal | logical | resolves | enforced | local",
        description="A set of flags that defines how references are supported.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["literal", "logical", "resolves", "enforced", "local"],
    )
    referencePolicy__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_referencePolicy", title="Extension field for ``referencePolicy``."
    )

    searchInclude: ListType[fhirtypes.String] = Field(
        None,
        alias="searchInclude",
        title="_include values supported by the server",
        description="A list of _include values supported by the server.",
    )
    searchInclude__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_searchInclude", title="Extension field for ``searchInclude``."
    )

    searchParam: ListType[
        fhirtypes.CapabilityStatementRestResourceSearchParamType
    ] = Field(
        None,
        alias="searchParam",
        title="Search parameters supported by implementation",
        description=(
            "Search parameters for implementations to support and/or make use of - "
            "either references to ones defined in the specification, or additional "
            "ones defined for/by the implementation."
        ),
    )

    searchRevInclude: ListType[fhirtypes.String] = Field(
        None,
        alias="searchRevInclude",
        title="_revinclude values supported by the server",
        description=(
            "A list of _revinclude (reverse include) values supported by the " "server."
        ),
    )
    searchRevInclude__ext: ListType[
        Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_searchRevInclude",
        title="Extension field for ``searchRevInclude``.",
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="A resource type that is supported",
        description="A type of resource exposed via the restful interface.",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    updateCreate: bool = Field(
        None,
        alias="updateCreate",
        title="If update can commit to a new identity",
        description=(
            "A flag to indicate that the server allows or needs to allow the client"
            " to create new identities on the server (e.g. that is, the client PUTs"
            " to a location where there is no existing resource). Allowing this "
            "operation means that the server allows the client to create new "
            "identities on the server."
        ),
    )
    updateCreate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_updateCreate", title="Extension field for ``updateCreate``."
    )

    versioning: fhirtypes.Code = Field(
        None,
        alias="versioning",
        title="no-version | versioned | versioned-update",
        description=(
            "This field is set to no-version to specify that the system does not "
            "support (server) or use (client) versioning for this resource type. If"
            " this has some other value, the server must at least correctly track "
            "and populate the versionId meta-property on resources. If the value is"
            " 'versioned-update', then the server supports all the versioning "
            "features, including using e-tags for version integrity in the API."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["no-version", "versioned", "versioned-update"],
    )
    versioning__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_versioning", title="Extension field for ``versioning``."
    )


class CapabilityStatementRestResourceInteraction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What operations are supported?.
    Identifies a restful operation supported by the solution.
    """

    resource_type = Field("CapabilityStatementRestResourceInteraction", const=True)

    code: fhirtypes.Code = Field(
        ...,
        alias="code",
        title=(
            "read | vread | update | patch | delete | history-instance | history-"
            "type | create | search-type"
        ),
        description="Coded identifier of the operation, supported by the system resource.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "read",
            "vread",
            "update",
            "patch",
            "delete",
            "history-instance",
            "history-type",
            "create",
            "search-type",
        ],
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Anything special about operation behavior",
        description=(
            "Guidance specific to the implementation of this operation, such as "
            "'delete is a logical delete' or 'updates are only allowed with version"
            " id' or 'creates permitted from pre-authorized certificates only'."
        ),
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )


class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Search parameters supported by implementation.
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """

    resource_type = Field("CapabilityStatementRestResourceSearchParam", const=True)

    definition: fhirtypes.Uri = Field(
        None,
        alias="definition",
        title="Source of definition for parameter",
        description=(
            "An absolute URI that is a formal reference to where this parameter was"
            " first defined, so that a client can be confident of the meaning of "
            "the search parameter (a reference to [SearchParameter.url]())."
        ),
    )
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definition", title="Extension field for ``definition``."
    )

    documentation: fhirtypes.String = Field(
        None,
        alias="documentation",
        title="Server-specific usage",
        description=(
            "This allows documentation of any distinct behaviors about how the "
            "search parameter is used.  For example, text matching algorithms."
        ),
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name of search parameter",
        description="The name of the search parameter used in the interface.",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title=(
            "number | date | string | token | reference | composite | quantity | " "uri"
        ),
        description=(
            "The type of value a search parameter refers to, and how the content is"
            " interpreted."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "number",
            "date",
            "string",
            "token",
            "reference",
            "composite",
            "quantity",
            "uri",
        ],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class CapabilityStatementRestSecurity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about security of implementation.
    Information about security implementation from an interface perspective -
    what a client needs to know.
    """

    resource_type = Field("CapabilityStatementRestSecurity", const=True)

    certificate: ListType[
        fhirtypes.CapabilityStatementRestSecurityCertificateType
    ] = Field(
        None,
        alias="certificate",
        title="Certificates associated with security profiles",
        description=None,
    )

    cors: bool = Field(
        None,
        alias="cors",
        title="Adds CORS Headers (http://enable-cors.org/)",
        description=(
            "Server adds CORS headers when responding to requests - this enables "
            "javascript applications to use the server."
        ),
    )
    cors__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_cors", title="Extension field for ``cors``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="General description of how security works",
        description=None,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    service: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="service",
        title="OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates",
        description="Types of security services that are supported/required by the system.",
    )


class CapabilityStatementRestSecurityCertificate(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Certificates associated with security profiles.
    """

    resource_type = Field("CapabilityStatementRestSecurityCertificate", const=True)

    blob: fhirtypes.Base64Binary = Field(
        None, alias="blob", title="Actual certificate", description=None,
    )
    blob__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_blob", title="Extension field for ``blob``."
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="Mime type for certificates",
        description="Mime type for a certificate.",
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class CapabilityStatementSoftware(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Software that is covered by this capability statement.
    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """

    resource_type = Field("CapabilityStatementSoftware", const=True)

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="A name the software is known by",
        description="Name software is known by.",
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    releaseDate: fhirtypes.DateTime = Field(
        None,
        alias="releaseDate",
        title="Date this version released",
        description="Date this version of the software was released.",
    )
    releaseDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_releaseDate", title="Extension field for ``releaseDate``."
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Version covered by this statement",
        description="The version identifier for the software covered by this statement.",
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
    )
