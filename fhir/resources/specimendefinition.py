# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SpecimenDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class SpecimenDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Kind of specimen.
    A kind of specimen with associated set of requirements.
    """

    resource_type = Field("SpecimenDefinition", const=True)

    collection: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="collection",
        title="Specimen collection procedure",
        description="The action to be performed for collecting the specimen.",
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Business identifier of a kind of specimen",
        description="A business identifier associated with the kind of specimen.",
    )

    patientPreparation: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="patientPreparation",
        title="Patient preparation for collection",
        description="Preparation of the patient for specimen collection.",
    )

    timeAspect: fhirtypes.String = Field(
        None,
        alias="timeAspect",
        title="Time aspect for collection",
        description="Time aspect of specimen collection (duration or offset).",
    )
    timeAspect__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timeAspect", title="Extension field for ``timeAspect``."
    )

    typeCollected: fhirtypes.CodeableConceptType = Field(
        None,
        alias="typeCollected",
        title="Kind of material to collect",
        description="The kind of material to be collected.",
    )

    typeTested: ListType[fhirtypes.SpecimenDefinitionTypeTestedType] = Field(
        None,
        alias="typeTested",
        title="Specimen in container intended for testing by lab",
        description=(
            "Specimen conditioned in a container as expected by the testing "
            "laboratory."
        ),
    )


class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specimen in container intended for testing by lab.
    Specimen conditioned in a container as expected by the testing laboratory.
    """

    resource_type = Field("SpecimenDefinitionTypeTested", const=True)

    container: fhirtypes.SpecimenDefinitionTypeTestedContainerType = Field(
        None, alias="container", title="The specimen's container", description=None,
    )

    handling: ListType[fhirtypes.SpecimenDefinitionTypeTestedHandlingType] = Field(
        None,
        alias="handling",
        title="Specimen handling before testing",
        description=(
            "Set of instructions for preservation/transport of the specimen at a "
            "defined temperature interval, prior the testing process."
        ),
    )

    isDerived: bool = Field(
        None,
        alias="isDerived",
        title="Primary or secondary specimen",
        description="Primary of secondary specimen.",
    )
    isDerived__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_isDerived", title="Extension field for ``isDerived``."
    )

    preference: fhirtypes.Code = Field(
        ...,
        alias="preference",
        title="preferred | alternate",
        description="The preference for this type of conditioned specimen.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["preferred", "alternate"],
    )
    preference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preference", title="Extension field for ``preference``."
    )

    rejectionCriterion: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="rejectionCriterion",
        title="Rejection criterion",
        description=(
            "Criterion for rejection of the specimen in its container by the "
            "laboratory."
        ),
    )

    requirement: fhirtypes.String = Field(
        None,
        alias="requirement",
        title="Specimen requirements",
        description=(
            "Requirements for delivery and special handling of this kind of "
            "conditioned specimen."
        ),
    )
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_requirement", title="Extension field for ``requirement``."
    )

    retentionTime: fhirtypes.DurationType = Field(
        None,
        alias="retentionTime",
        title="Specimen retention time",
        description=(
            "The usual time that a specimen of this kind is retained after the "
            "ordered tests are completed, for the purpose of additional testing."
        ),
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type of intended specimen",
        description="The kind of specimen conditioned for testing expected by lab.",
    )


class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The specimen's container.
    """

    resource_type = Field("SpecimenDefinitionTypeTestedContainer", const=True)

    additive: ListType[
        fhirtypes.SpecimenDefinitionTypeTestedContainerAdditiveType
    ] = Field(
        None,
        alias="additive",
        title="Additive associated with container",
        description=(
            "Substance introduced in the kind of container to preserve, maintain or"
            " enhance the specimen. Examples: Formalin, Citrate, EDTA."
        ),
    )

    cap: fhirtypes.CodeableConceptType = Field(
        None, alias="cap", title="Color of container cap", description=None,
    )

    capacity: fhirtypes.QuantityType = Field(
        None,
        alias="capacity",
        title="Container capacity",
        description="The capacity (volume or other measure) of this kind of container.",
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Container description",
        description="The textual description of the kind of container.",
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    material: fhirtypes.CodeableConceptType = Field(
        None,
        alias="material",
        title="Container material",
        description="The type of material of the container.",
    )

    minimumVolumeQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="minimumVolumeQuantity",
        title="Minimum volume",
        description="The minimum volume to be conditioned in the container.",
        # Choice of Data Types. i.e minimumVolume[x]
        one_of_many="minimumVolume",
        one_of_many_required=False,
    )

    minimumVolumeString: fhirtypes.String = Field(
        None,
        alias="minimumVolumeString",
        title="Minimum volume",
        description="The minimum volume to be conditioned in the container.",
        # Choice of Data Types. i.e minimumVolume[x]
        one_of_many="minimumVolume",
        one_of_many_required=False,
    )
    minimumVolumeString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_minimumVolumeString",
        title="Extension field for ``minimumVolumeString``.",
    )

    preparation: fhirtypes.String = Field(
        None,
        alias="preparation",
        title="Specimen container preparation",
        description=(
            "Special processing that should be applied to the container for this "
            "kind of specimen."
        ),
    )
    preparation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preparation", title="Extension field for ``preparation``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Kind of container associated with the kind of specimen",
        description="The type of container used to contain this kind of specimen.",
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
            "minimumVolume": ["minimumVolumeQuantity", "minimumVolumeString"]
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


class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additive associated with container.
    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """

    resource_type = Field("SpecimenDefinitionTypeTestedContainerAdditive", const=True)

    additiveCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="additiveCodeableConcept",
        title="Additive associated with container",
        description=(
            "Substance introduced in the kind of container to preserve, maintain or"
            " enhance the specimen. Examples: Formalin, Citrate, EDTA."
        ),
        # Choice of Data Types. i.e additive[x]
        one_of_many="additive",
        one_of_many_required=True,
    )

    additiveReference: fhirtypes.ReferenceType = Field(
        None,
        alias="additiveReference",
        title="Additive associated with container",
        description=(
            "Substance introduced in the kind of container to preserve, maintain or"
            " enhance the specimen. Examples: Formalin, Citrate, EDTA."
        ),
        # Choice of Data Types. i.e additive[x]
        one_of_many="additive",
        one_of_many_required=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Substance"],
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
            "additive": ["additiveCodeableConcept", "additiveReference"]
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


class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Specimen handling before testing.
    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """

    resource_type = Field("SpecimenDefinitionTypeTestedHandling", const=True)

    instruction: fhirtypes.String = Field(
        None,
        alias="instruction",
        title="Preservation instruction",
        description=(
            "Additional textual instructions for the preservation or transport of "
            "the specimen. For instance, 'Protect from light exposure'."
        ),
    )
    instruction__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_instruction", title="Extension field for ``instruction``."
    )

    maxDuration: fhirtypes.DurationType = Field(
        None,
        alias="maxDuration",
        title="Maximum preservation time",
        description=(
            "The maximum time interval of preservation of the specimen with these "
            "conditions."
        ),
    )

    temperatureQualifier: fhirtypes.CodeableConceptType = Field(
        None,
        alias="temperatureQualifier",
        title="Temperature qualifier",
        description=(
            "It qualifies the interval of temperature, which characterizes an "
            "occurrence of handling. Conditions that are not related to temperature"
            " may be handled in the instruction element."
        ),
    )

    temperatureRange: fhirtypes.RangeType = Field(
        None,
        alias="temperatureRange",
        title="Temperature range",
        description="The temperature interval for this set of handling instructions.",
    )
