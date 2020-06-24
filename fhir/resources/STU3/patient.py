# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class Patient(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Information about an individual or animal receiving health care services.
    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    resource_type = Field("Patient", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this patient's record is in active use",
        description="Whether this patient record is in active use.",
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    address: ListType[fhirtypes.AddressType] = Field(
        None, alias="address", title="Addresses for the individual", description=None,
    )

    animal: fhirtypes.PatientAnimalType = Field(
        None,
        alias="animal",
        title="This patient is known to be an animal (non-human)",
        description="This patient is known to be an animal.",
    )

    birthDate: fhirtypes.Date = Field(
        None,
        alias="birthDate",
        title="The date of birth for the individual",
        description=None,
    )
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_birthDate", title="Extension field for ``birthDate``."
    )

    communication: ListType[fhirtypes.PatientCommunicationType] = Field(
        None,
        alias="communication",
        title=(
            "A list of Languages which may be used to communicate with the patient "
            "about his or her health"
        ),
        description=(
            "Languages which may be used to communicate with the patient about his "
            "or her health."
        ),
    )

    contact: ListType[fhirtypes.PatientContactType] = Field(
        None,
        alias="contact",
        title="A contact party (e.g. guardian, partner, friend) for the patient",
        description=None,
    )

    deceasedBoolean: bool = Field(
        None,
        alias="deceasedBoolean",
        title="Indicates if the individual is deceased or not",
        description=None,
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_deceasedBoolean", title="Extension field for ``deceasedBoolean``."
    )

    deceasedDateTime: fhirtypes.DateTime = Field(
        None,
        alias="deceasedDateTime",
        title="Indicates if the individual is deceased or not",
        description=None,
        # Choice of Data Types. i.e deceased[x]
        one_of_many="deceased",
        one_of_many_required=False,
    )
    deceasedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_deceasedDateTime",
        title="Extension field for ``deceasedDateTime``.",
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that the patient is considered to "
            "have for administration and record keeping purposes."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["male", "female", "other", "unknown"],
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    generalPractitioner: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="generalPractitioner",
        title="Patient's nominated primary care provider",
        description="Patient's nominated care provider.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization", "Practitioner"],
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="An identifier for this patient",
        description=None,
    )

    link: ListType[fhirtypes.PatientLinkType] = Field(
        None,
        alias="link",
        title="Link to another patient resource that concerns the same actual person",
        description=(
            "Link to another patient resource that concerns the same actual " "patient."
        ),
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="Organization that is the custodian of the patient record",
        description=None,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    maritalStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="maritalStatus",
        title="Marital (civil) status of a patient",
        description="This field contains a patient's most recent marital (civil) status.",
    )

    multipleBirthBoolean: bool = Field(
        None,
        alias="multipleBirthBoolean",
        title="Whether patient is part of a multiple birth",
        description=(
            "Indicates whether the patient is part of a multiple (bool) or "
            "indicates the actual birth order (integer)."
        ),
        # Choice of Data Types. i.e multipleBirth[x]
        one_of_many="multipleBirth",
        one_of_many_required=False,
    )
    multipleBirthBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_multipleBirthBoolean",
        title="Extension field for ``multipleBirthBoolean``.",
    )

    multipleBirthInteger: fhirtypes.Integer = Field(
        None,
        alias="multipleBirthInteger",
        title="Whether patient is part of a multiple birth",
        description=(
            "Indicates whether the patient is part of a multiple (bool) or "
            "indicates the actual birth order (integer)."
        ),
        # Choice of Data Types. i.e multipleBirth[x]
        one_of_many="multipleBirth",
        one_of_many_required=False,
    )
    multipleBirthInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_multipleBirthInteger",
        title="Extension field for ``multipleBirthInteger``.",
    )

    name: ListType[fhirtypes.HumanNameType] = Field(
        None,
        alias="name",
        title="A name associated with the patient",
        description="A name associated with the individual.",
    )

    photo: ListType[fhirtypes.AttachmentType] = Field(
        None, alias="photo", title="Image of the patient", description=None,
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="A contact detail for the individual",
        description=(
            "A contact detail (e.g. a telephone number or an email address) by "
            "which the individual may be contacted."
        ),
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
            "deceased": ["deceasedBoolean", "deceasedDateTime"],
            "multipleBirth": ["multipleBirthBoolean", "multipleBirthInteger"],
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


class PatientAnimal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    This patient is known to be an animal (non-human).
    This patient is known to be an animal.
    """

    resource_type = Field("PatientAnimal", const=True)

    breed: fhirtypes.CodeableConceptType = Field(
        None,
        alias="breed",
        title="E.g. Poodle, Angus",
        description="Identifies the detailed categorization of the kind of animal.",
    )

    genderStatus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="genderStatus",
        title="E.g. Neutered, Intact",
        description="Indicates the current state of the animal's reproductive organs.",
    )

    species: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="species",
        title="E.g. Dog, Cow",
        description=(
            "Identifies the high level taxonomic categorization of the kind of "
            "animal."
        ),
    )


class PatientCommunication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A list of Languages which may be used to communicate with the patient about
    his or her health.
    Languages which may be used to communicate with the patient about his or
    her health.
    """

    resource_type = Field("PatientCommunication", const=True)

    language: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="language",
        title=(
            "The language which can be used to communicate with the patient about "
            "his or her health"
        ),
        description=(
            "The ISO-639-1 alpha 2 code in lower case for the language, optionally "
            "followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in"
            ' upper case; e.g. "en" for English, or "en-US" for American English '
            'versus "en-EN" for England English.'
        ),
    )

    preferred: bool = Field(
        None,
        alias="preferred",
        title="Language preference indicator",
        description=(
            "Indicates whether or not the patient prefers this language (over other"
            " languages he masters up a certain level)."
        ),
    )
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preferred", title="Extension field for ``preferred``."
    )


class PatientContact(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A contact party (e.g. guardian, partner, friend) for the patient.
    """

    resource_type = Field("PatientContact", const=True)

    address: fhirtypes.AddressType = Field(
        None, alias="address", title="Address for the contact person", description=None,
    )

    gender: fhirtypes.Code = Field(
        None,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that the contact person is "
            "considered to have for administration and record keeping purposes."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["male", "female", "other", "unknown"],
    )
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_gender", title="Extension field for ``gender``."
    )

    name: fhirtypes.HumanNameType = Field(
        None,
        alias="name",
        title="A name associated with the contact person",
        description=None,
    )

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Organization that is associated with the contact",
        description=(
            "Organization on behalf of which the contact is acting or for which the"
            " contact is working."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title=(
            "The period during which this contact person or organization is valid "
            "to be contacted relating to this patient"
        ),
        description=None,
    )

    relationship: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="relationship",
        title="The kind of relationship",
        description=(
            "The nature of the relationship between the patient and the contact "
            "person."
        ),
    )

    telecom: ListType[fhirtypes.ContactPointType] = Field(
        None,
        alias="telecom",
        title="A contact detail for the person",
        description=(
            "A contact detail for the person, e.g. a telephone number or an email "
            "address."
        ),
    )


class PatientLink(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Link to another patient resource that concerns the same actual person.
    Link to another patient resource that concerns the same actual patient.
    """

    resource_type = Field("PatientLink", const=True)

    other: fhirtypes.ReferenceType = Field(
        ...,
        alias="other",
        title="The other patient or related person resource that the link refers to",
        description="The other patient resource that the link refers to.",
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "RelatedPerson"],
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="replaced-by | replaces | refer | seealso - type of link",
        description=(
            "The type of link between this patient resource and another patient "
            "resource."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["replaced-by", "replaces", "refer", "seealso - type of link"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
