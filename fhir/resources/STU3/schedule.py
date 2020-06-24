# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Schedule
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import domainresource, fhirtypes


class Schedule(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A container for slots of time that may be available for booking
    appointments.
    """

    resource_type = Field("Schedule", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this schedule is in active use",
        description=(
            "Whether this schedule record is in active use, or should not be used "
            "(such as was entered in error)."
        ),
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    actor: ListType[fhirtypes.ReferenceType] = Field(
        ...,
        alias="actor",
        title=(
            "The resource this Schedule resource is providing availability "
            "information for. These are expected to usually be one of "
            "HealthcareService, Location, Practitioner, PractitionerRole, Device, "
            "Patient or RelatedPerson"
        ),
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "Patient",
            "Practitioner",
            "PractitionerRole",
            "RelatedPerson",
            "Device",
            "HealthcareService",
            "Location",
        ],
    )

    comment: fhirtypes.String = Field(
        None,
        alias="comment",
        title=(
            "Comments on the availability to describe any extended information. "
            "Such as custom constraints on the slots that may be associated"
        ),
        description=None,
    )
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_comment", title="Extension field for ``comment``."
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None, alias="identifier", title="External Ids for this item", description=None,
    )

    planningHorizon: fhirtypes.PeriodType = Field(
        None,
        alias="planningHorizon",
        title=(
            "The period of time that the slots that are attached to this Schedule "
            "resource cover (even if none exist). These  cover the amount of time "
            "that an organization's planning horizon; the interval for which they "
            "are currently accepting appointments. This does not define a "
            '"template" for planning outside these dates'
        ),
        description=None,
    )

    serviceCategory: fhirtypes.CodeableConceptType = Field(
        None,
        alias="serviceCategory",
        title=(
            "A broad categorisation of the service that is to be performed during "
            "this appointment"
        ),
        description=None,
    )

    serviceType: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="serviceType",
        title="The specific service that is to be performed during this appointment",
        description=None,
    )

    specialty: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialty",
        title=(
            "The specialty of a practitioner that would be required to perform the "
            "service requested in this appointment"
        ),
        description=None,
    )
