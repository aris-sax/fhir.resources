# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Communication
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Communication(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A record of information transmitted from a sender to a receiver.
    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency was notified about a
    reportable condition.
    """

    resource_type = Field("Communication", const=True)

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Request fulfilled by this communication",
        description=(
            "An order, proposal or plan fulfilled in whole or in part by this "
            "Communication."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    category: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Message category",
        description=(
            "The type of message conveyed such as alert, notification, reminder, "
            "instruction, etc."
        ),
    )

    context: fhirtypes.ReferenceType = Field(
        None,
        alias="context",
        title="Encounter or episode leading to message",
        description="The encounter within which the communication was sent.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Encounter", "EpisodeOfCare"],
    )

    definition: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="definition",
        title="Instantiates protocol or definition",
        description=(
            "A protocol, guideline, or other definition that was adhered to in "
            "whole or in part by this communication event."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["PlanDefinition", "ActivityDefinition"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique identifier",
        description=(
            "Identifiers associated with this Communication that are defined by "
            "business processes and/ or used to refer to it when a direct URL "
            "reference to the resource itself is not appropriate (e.g. in CDA "
            "documents, or in written / printed documentation)."
        ),
    )

    medium: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="medium",
        title="A channel of communication",
        description="A channel that was used for this communication (e.g. email, fax).",
    )

    notDone: bool = Field(
        None,
        alias="notDone",
        title="Communication did not occur",
        description=(
            "If true, indicates that the described communication event did not "
            "actually occur."
        ),
    )
    notDone__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_notDone", title="Extension field for ``notDone``."
    )

    notDoneReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="notDoneReason",
        title="Why communication did not occur",
        description=(
            "Describes why the communication event did not occur in coded and/or "
            "textual form."
        ),
    )

    note: ListType[fhirtypes.AnnotationType] = Field(
        None,
        alias="note",
        title="Comments made about the communication",
        description=(
            "Additional notes or commentary about the communication by the sender, "
            "receiver or other interested parties."
        ),
    )

    partOf: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="partOf",
        title="Part of this action",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    payload: ListType[fhirtypes.CommunicationPayloadType] = Field(
        None,
        alias="payload",
        title="Message payload",
        description=(
            "Text, attachment(s), or resource(s) that was communicated to the "
            "recipient."
        ),
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="Indication for message",
        description="The reason or justification for the communication.",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title="Why was communication done?",
        description=(
            "Indicates another resource whose existence justifies this "
            "communication."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Condition", "Observation"],
    )

    received: fhirtypes.DateTime = Field(
        None,
        alias="received",
        title="When received",
        description="The time when this communication arrived at the destination.",
    )
    received__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_received", title="Extension field for ``received``."
    )

    recipient: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="recipient",
        title="Message recipient",
        description=(
            "The entity (e.g. person, organization, clinical information system, or"
            " device) which was the target of the communication. If receipts need "
            "to be tracked by individual, a separate resource instance will need to"
            " be created for each recipient. \u00a0Multiple recipient communications are"
            " intended where either a receipt(s) is not tracked (e.g. a mass mail-"
            "out) or is captured in aggregate (all emails confirmed received by a "
            "particular time)."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Organization",
            "Patient",
            "Practitioner",
            "RelatedPerson",
            "Group",
        ],
    )

    sender: fhirtypes.ReferenceType = Field(
        None,
        alias="sender",
        title="Message sender",
        description=(
            "The entity (e.g. person, organization, clinical information system, or"
            " device) which was the source of the communication."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Device",
            "Organization",
            "Patient",
            "Practitioner",
            "RelatedPerson",
        ],
    )

    sent: fhirtypes.DateTime = Field(
        None,
        alias="sent",
        title="When sent",
        description="The time when this communication was sent.",
    )
    sent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sent", title="Extension field for ``sent``."
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title=(
            "preparation | in-progress | suspended | aborted | completed | entered-"
            "in-error"
        ),
        description="The status of the transmission.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "preparation",
            "in-progress",
            "suspended",
            "aborted",
            "completed",
            "entered-in-error",
        ],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title="Focus of message",
        description="The patient or group that was the focus of this communication.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Group"],
    )

    topic: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="topic",
        title="Focal resources",
        description=(
            "The resources which were responsible for or related to producing this "
            "communication."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )


class CommunicationPayload(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Message payload.
    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """

    resource_type = Field("CommunicationPayload", const=True)

    contentAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="contentAttachment",
        title="Message part content",
        description=(
            "A communicated content (or for multi-part communications, one portion "
            "of the communication)."
        ),
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
    )

    contentReference: fhirtypes.ReferenceType = Field(
        None,
        alias="contentReference",
        title="Message part content",
        description=(
            "A communicated content (or for multi-part communications, one portion "
            "of the communication)."
        ),
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    contentString: fhirtypes.String = Field(
        None,
        alias="contentString",
        title="Message part content",
        description=(
            "A communicated content (or for multi-part communications, one portion "
            "of the communication)."
        ),
        # Choice of Data Types. i.e content[x]
        one_of_many="content",
        one_of_many_required=True,
    )
    contentString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_contentString", title="Extension field for ``contentString``."
    )

    @root_validator(pre=True)
    def validate_one_of_many(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "content": ["contentAttachment", "contentReference", "contentString"]
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
