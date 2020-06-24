# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import Any, Dict
from typing import List as ListType
from typing import Union

from pydantic import Field, root_validator

from . import backboneelement, domainresource, fhirtypes


class PlanDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The definition of a plan for a series of actions, independent of any
    specific patient or context.
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    resource_type = Field("PlanDefinition", const=True)

    action: ListType[fhirtypes.PlanDefinitionActionType] = Field(
        None,
        alias="action",
        title="Action defined by the plan",
        description="An action or group of actions to be taken as part of the plan.",
    )

    approvalDate: fhirtypes.Date = Field(
        None,
        alias="approvalDate",
        title="When the plan definition was approved by publisher",
        description=(
            "The date on which the resource content was approved by the publisher. "
            "Approval happens once when the content is officially approved for "
            "usage."
        ),
    )
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_approvalDate", title="Extension field for ``approvalDate``."
    )

    author: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="author",
        title="Who authored the content",
        description=(
            "An individiual or organization primarily involved in the creation and "
            "maintenance of the content."
        ),
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
            "A copyright statement relating to the plan definition and/or its "
            "contents. Copyright statements are generally legal restrictions on the"
            " use and publishing of the plan definition."
        ),
    )
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_copyright", title="Extension field for ``copyright``."
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the plan definition was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the plan definition changes."
        ),
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the plan definition",
        description=(
            "A free text natural language description of the plan definition from a"
            " consumer's perspective."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    editor: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="editor",
        title="Who edited the content",
        description=(
            "An individual or organization primarily responsible for internal "
            "coherence of the content."
        ),
    )

    effectivePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="effectivePeriod",
        title="When the plan definition is expected to be used",
        description=(
            "The period during which the plan definition content was or is planned "
            "to be in active use."
        ),
    )

    endorser: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="endorser",
        title="Who endorsed the content",
        description=(
            "An individual or organization responsible for officially endorsing the"
            " content for use in some setting."
        ),
    )

    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this plan definition is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    goal: ListType[fhirtypes.PlanDefinitionGoalType] = Field(
        None,
        alias="goal",
        title="What the plan is trying to accomplish",
        description=(
            "Goals that describe what the activities within the plan are intended "
            "to achieve. For example, weight loss, restoring an activity of daily "
            "living, obtaining herd immunity via immunization, meeting a process "
            "improvement objective, etc."
        ),
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Additional identifier for the plan definition",
        description=(
            "A formal identifier that is used to identify this plan definition when"
            " it is represented in other formats, or referenced in a specification,"
            " model, design or an instance."
        ),
    )

    jurisdiction: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for plan definition (if applicable)",
        description=(
            "A legal or geographic region in which the plan definition is intended "
            "to be used."
        ),
    )

    lastReviewDate: fhirtypes.Date = Field(
        None,
        alias="lastReviewDate",
        title="When the plan definition was last reviewed",
        description=(
            "The date on which the resource content was last reviewed. Review "
            "happens periodically after approval but does not change the original "
            "approval date."
        ),
    )
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_lastReviewDate", title="Extension field for ``lastReviewDate``."
    )

    library: ListType[fhirtypes.Canonical] = Field(
        None,
        alias="library",
        title="Logic used by the plan definition",
        description=(
            "A reference to a Library resource containing any formal logic used by "
            "the plan definition."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Library"],
    )
    library__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_library", title="Extension field for ``library``."
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this plan definition (computer friendly)",
        description=(
            "A natural language name identifying the plan definition. This name "
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
            "The name of the organization or individual that published the plan "
            "definition."
        ),
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this plan definition is defined",
        description=(
            "Explanation of why this plan definition is needed and why it has been "
            "designed as it has."
        ),
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    relatedArtifact: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="relatedArtifact",
        title="Additional documentation, citations",
        description=(
            "Related artifacts such as additional documentation, justification, or "
            "bibliographic references."
        ),
    )

    reviewer: ListType[fhirtypes.ContactDetailType] = Field(
        None,
        alias="reviewer",
        title="Who reviewed the content",
        description=(
            "An individual or organization primarily responsible for review of some"
            " aspect of the content."
        ),
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this plan definition. Enables tracking the life-cycle of"
            " the content."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title="Type of individual the plan definition is focused on",
        description=(
            "A code or group definition that describes the intended subject of the "
            "plan definition."
        ),
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title="Type of individual the plan definition is focused on",
        description=(
            "A code or group definition that describes the intended subject of the "
            "plan definition."
        ),
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    subtitle: fhirtypes.String = Field(
        None,
        alias="subtitle",
        title="Subordinate title of the plan definition",
        description=(
            "An explanatory or alternate title for the plan definition giving "
            "additional information about its content."
        ),
    )
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_subtitle", title="Extension field for ``subtitle``."
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this plan definition (human friendly)",
        description="A short, descriptive, user-friendly title for the plan definition.",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    topic: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="topic",
        title="E.g. Education, Treatment, Assessment",
        description=(
            "Descriptive topics related to the content of the plan definition. "
            "Topics provide a high-level categorization of the definition that can "
            "be useful for filtering and searching."
        ),
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="order-set | clinical-protocol | eca-rule | workflow-definition",
        description=(
            "A high-level category for the plan definition that distinguishes the "
            "kinds of systems that would be interested in the plan definition."
        ),
    )

    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this plan definition, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this plan definition when it "
            "is referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which at which an authoritative "
            "instance of this plan definition is (or will be) published. This URL "
            "can be the target of a canonical reference. It SHALL remain the same "
            "when the plan definition is stored on different servers."
        ),
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_url", title="Extension field for ``url``."
    )

    usage: fhirtypes.String = Field(
        None,
        alias="usage",
        title="Describes the clinical usage of the plan",
        description=(
            "A detailed description of how the plan definition is used from a "
            "clinical perspective."
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
            "indexing and searching for appropriate plan definition instances."
        ),
    )

    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the plan definition",
        description=(
            "The identifier that is used to identify this version of the plan "
            "definition when it is referenced in a specification, model, design or "
            "instance. This is an arbitrary value managed by the plan definition "
            "author and is not expected to be globally unique. For example, it "
            "might be a timestamp (e.g. yyyymmdd) if a managed version is not "
            "available. There is also no expectation that versions can be placed in"
            " a lexicographical sequence. To provide a version consistent with the "
            "Decision Support Service specification, use the format "
            "Major.Minor.Revision (e.g. 1.0.0). For more information on versioning "
            "knowledge assets, refer to the Decision Support Service specification."
            " Note that a version is required for non-experimental active "
            "artifacts."
        ),
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_version", title="Extension field for ``version``."
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
        one_of_many_fields = {"subject": ["subjectCodeableConcept", "subjectReference"]}
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


class PlanDefinitionAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Action defined by the plan.
    An action or group of actions to be taken as part of the plan.
    """

    resource_type = Field("PlanDefinitionAction", const=True)

    action: ListType[fhirtypes.PlanDefinitionActionType] = Field(
        None,
        alias="action",
        title="A sub-action",
        description=(
            "Sub actions that are contained within the action. The behavior of this"
            " action determines the functionality of the sub-actions. For example, "
            "a selection behavior of at-most-one indicates that of the sub-actions,"
            " at most one may be chosen as part of realizing the action definition."
        ),
    )

    cardinalityBehavior: fhirtypes.Code = Field(
        None,
        alias="cardinalityBehavior",
        title="single | multiple",
        description="Defines whether the action can be selected multiple times.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["single", "multiple"],
    )
    cardinalityBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_cardinalityBehavior",
        title="Extension field for ``cardinalityBehavior``.",
    )

    code: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="code",
        title="Code representing the meaning of the action or sub-actions",
        description=(
            "A code that provides meaning for the action or action group. For "
            "example, a section may have a LOINC code for the section of a "
            "documentation template."
        ),
    )

    condition: ListType[fhirtypes.PlanDefinitionActionConditionType] = Field(
        None,
        alias="condition",
        title="Whether or not the action is applicable",
        description=(
            "An expression that describes applicability criteria or start/stop "
            "conditions for the action."
        ),
    )

    definitionCanonical: fhirtypes.Canonical = Field(
        None,
        alias="definitionCanonical",
        title="Description of the activity to be performed",
        description=(
            "A reference to an ActivityDefinition that describes the action to be "
            "taken in detail, or a PlanDefinition that describes a series of "
            "actions to be taken."
        ),
        # Choice of Data Types. i.e definition[x]
        one_of_many="definition",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ActivityDefinition", "PlanDefinition", "Questionnaire"],
    )
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_definitionCanonical",
        title="Extension field for ``definitionCanonical``.",
    )

    definitionUri: fhirtypes.Uri = Field(
        None,
        alias="definitionUri",
        title="Description of the activity to be performed",
        description=(
            "A reference to an ActivityDefinition that describes the action to be "
            "taken in detail, or a PlanDefinition that describes a series of "
            "actions to be taken."
        ),
        # Choice of Data Types. i.e definition[x]
        one_of_many="definition",
        one_of_many_required=False,
    )
    definitionUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_definitionUri", title="Extension field for ``definitionUri``."
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Brief description of the action",
        description=(
            "A brief description of the action used to provide a summary to display"
            " to the user."
        ),
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    documentation: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="documentation",
        title="Supporting documentation for the intended performer of the action",
        description=(
            "Didactic or other informational resources associated with the action "
            "that can be provided to the CDS recipient. Information resources can "
            "include inline text commentary and links to web resources."
        ),
    )

    dynamicValue: ListType[fhirtypes.PlanDefinitionActionDynamicValueType] = Field(
        None,
        alias="dynamicValue",
        title="Dynamic aspects of the definition",
        description=(
            "Customizations that should be applied to the statically defined "
            "resource. For example, if the dosage of a medication must be computed "
            "based on the patient's weight, a customization would be used to "
            "specify an expression that calculated the weight, and the path on the "
            "resource that would contain the result."
        ),
    )

    goalId: ListType[fhirtypes.Id] = Field(
        None,
        alias="goalId",
        title="What goals this action supports",
        description=(
            "Identifies goals that this action supports. The reference must be to a"
            " goal element defined within this plan definition."
        ),
    )
    goalId__ext: ListType[Union[fhirtypes.FHIRPrimitiveExtensionType, None]] = Field(
        None, alias="_goalId", title="Extension field for ``goalId``."
    )

    groupingBehavior: fhirtypes.Code = Field(
        None,
        alias="groupingBehavior",
        title="visual-group | logical-group | sentence-group",
        description="Defines the grouping behavior for the action and its children.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["visual-group", "logical-group", "sentence-group"],
    )
    groupingBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_groupingBehavior",
        title="Extension field for ``groupingBehavior``.",
    )

    input: ListType[fhirtypes.DataRequirementType] = Field(
        None,
        alias="input",
        title="Input data requirements",
        description="Defines input data requirements for the action.",
    )

    output: ListType[fhirtypes.DataRequirementType] = Field(
        None,
        alias="output",
        title="Output data definition",
        description="Defines the outputs of the action, if any.",
    )

    participant: ListType[fhirtypes.PlanDefinitionActionParticipantType] = Field(
        None,
        alias="participant",
        title="Who should participate in the action",
        description="Indicates who should participate in performing the action described.",
    )

    precheckBehavior: fhirtypes.Code = Field(
        None,
        alias="precheckBehavior",
        title="yes | no",
        description="Defines whether the action should usually be preselected.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["yes", "no"],
    )
    precheckBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_precheckBehavior",
        title="Extension field for ``precheckBehavior``.",
    )

    prefix: fhirtypes.String = Field(
        None,
        alias="prefix",
        title="User-visible prefix for the action (e.g. 1. or A.)",
        description="A user-visible prefix for the action.",
    )
    prefix__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_prefix", title="Extension field for ``prefix``."
    )

    priority: fhirtypes.Code = Field(
        None,
        alias="priority",
        title="routine | urgent | asap | stat",
        description=(
            "Indicates how quickly the action should be addressed with respect to "
            "other actions."
        ),
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["routine", "urgent", "asap", "stat"],
    )
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_priority", title="Extension field for ``priority``."
    )

    reason: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Why the action should be performed",
        description="A description of why this action is necessary or appropriate.",
    )

    relatedAction: ListType[fhirtypes.PlanDefinitionActionRelatedActionType] = Field(
        None,
        alias="relatedAction",
        title="Relationship to another action",
        description=(
            'A relationship to another action such as "before" or "30-60 minutes '
            'after start of".'
        ),
    )

    requiredBehavior: fhirtypes.Code = Field(
        None,
        alias="requiredBehavior",
        title="must | could | must-unless-documented",
        description="Defines the required behavior for the action.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["must", "could", "must-unless-documented"],
    )
    requiredBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_requiredBehavior",
        title="Extension field for ``requiredBehavior``.",
    )

    selectionBehavior: fhirtypes.Code = Field(
        None,
        alias="selectionBehavior",
        title="any | all | all-or-none | exactly-one | at-most-one | one-or-more",
        description="Defines the selection behavior for the action and its children.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "any",
            "all",
            "all-or-none",
            "exactly-one",
            "at-most-one",
            "one-or-more",
        ],
    )
    selectionBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_selectionBehavior",
        title="Extension field for ``selectionBehavior``.",
    )

    subjectCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subjectCodeableConcept",
        title="Type of individual the action is focused on",
        description=(
            "A code or group definition that describes the intended subject of the "
            "action and its children, if any."
        ),
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
    )

    subjectReference: fhirtypes.ReferenceType = Field(
        None,
        alias="subjectReference",
        title="Type of individual the action is focused on",
        description=(
            "A code or group definition that describes the intended subject of the "
            "action and its children, if any."
        ),
        # Choice of Data Types. i.e subject[x]
        one_of_many="subject",
        one_of_many_required=False,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Group"],
    )

    textEquivalent: fhirtypes.String = Field(
        None,
        alias="textEquivalent",
        title=(
            "Static text equivalent of the action, used if the dynamic aspects "
            "cannot be interpreted by the receiving system"
        ),
        description=(
            "A text equivalent of the action to be performed. This provides a "
            "human-interpretable description of the action when the definition is "
            "consumed by a system that might not be capable of interpreting it "
            "dynamically."
        ),
    )
    textEquivalent__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_textEquivalent", title="Extension field for ``textEquivalent``."
    )

    timingAge: fhirtypes.AgeType = Field(
        None,
        alias="timingAge",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingDateTime: fhirtypes.DateTime = Field(
        None,
        alias="timingDateTime",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_timingDateTime", title="Extension field for ``timingDateTime``."
    )

    timingDuration: fhirtypes.DurationType = Field(
        None,
        alias="timingDuration",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="timingPeriod",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingRange: fhirtypes.RangeType = Field(
        None,
        alias="timingRange",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    timingTiming: fhirtypes.TimingType = Field(
        None,
        alias="timingTiming",
        title="When the action should take place",
        description="An optional value describing when the action should be performed.",
        # Choice of Data Types. i.e timing[x]
        one_of_many="timing",
        one_of_many_required=False,
    )

    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="User-visible title",
        description="The title of the action displayed to a user.",
    )
    title__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_title", title="Extension field for ``title``."
    )

    transform: fhirtypes.Canonical = Field(
        None,
        alias="transform",
        title="Transform to apply the template",
        description=(
            "A reference to a StructureMap resource that defines a transform that "
            "can be executed to produce the intent resource using the "
            "ActivityDefinition instance as the input."
        ),
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["StructureMap"],
    )
    transform__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_transform", title="Extension field for ``transform``."
    )

    trigger: ListType[fhirtypes.TriggerDefinitionType] = Field(
        None,
        alias="trigger",
        title="When the action should be triggered",
        description="A description of when the action should be triggered.",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="create | update | remove | fire-event",
        description="The type of action to perform (create, update, remove).",
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
            "definition": ["definitionCanonical", "definitionUri"],
            "subject": ["subjectCodeableConcept", "subjectReference"],
            "timing": [
                "timingAge",
                "timingDateTime",
                "timingDuration",
                "timingPeriod",
                "timingRange",
                "timingTiming",
            ],
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


class PlanDefinitionActionCondition(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Whether or not the action is applicable.
    An expression that describes applicability criteria or start/stop
    conditions for the action.
    """

    resource_type = Field("PlanDefinitionActionCondition", const=True)

    expression: fhirtypes.ExpressionType = Field(
        None,
        alias="expression",
        title="Boolean-valued expression",
        description=(
            "An expression that returns true or false, indicating whether the "
            "condition is satisfied."
        ),
    )

    kind: fhirtypes.Code = Field(
        ...,
        alias="kind",
        title="applicability | start | stop",
        description="The kind of condition.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["applicability", "start", "stop"],
    )
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_kind", title="Extension field for ``kind``."
    )


class PlanDefinitionActionDynamicValue(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Dynamic aspects of the definition.
    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """

    resource_type = Field("PlanDefinitionActionDynamicValue", const=True)

    expression: fhirtypes.ExpressionType = Field(
        None,
        alias="expression",
        title="An expression that provides the dynamic value for the customization",
        description="An expression specifying the value of the customized element.",
    )

    path: fhirtypes.String = Field(
        None,
        alias="path",
        title="The path to the element to be set dynamically",
        description=(
            "The path to the element to be customized. This is the path on the "
            "resource that will hold the result of the calculation defined by the "
            "expression. The specified path SHALL be a FHIRPath resolveable on the "
            "specified target type of the ActivityDefinition, and SHALL consist "
            "only of identifiers, constant indexers, and a restricted subset of "
            "functions. The path is allowed to contain qualifiers (.) to traverse "
            "sub-elements, as well as indexers ([x]) to traverse multiple-"
            "cardinality sub-elements (see the [Simple FHIRPath "
            "Profile](fhirpath.html#simple) for full details)."
        ),
    )
    path__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_path", title="Extension field for ``path``."
    )


class PlanDefinitionActionParticipant(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Who should participate in the action.
    Indicates who should participate in performing the action described.
    """

    resource_type = Field("PlanDefinitionActionParticipant", const=True)

    role: fhirtypes.CodeableConceptType = Field(
        None,
        alias="role",
        title="E.g. Nurse, Surgeon, Parent",
        description=(
            "The role the participant should play in performing the described "
            "action."
        ),
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="patient | practitioner | related-person | device",
        description="The type of participant in the action.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["patient", "practitioner", "related-person", "device"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )


class PlanDefinitionActionRelatedAction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Relationship to another action.
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """

    resource_type = Field("PlanDefinitionActionRelatedAction", const=True)

    actionId: fhirtypes.Id = Field(
        ...,
        alias="actionId",
        title="What action is this related to",
        description="The element id of the related action.",
    )
    actionId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_actionId", title="Extension field for ``actionId``."
    )

    offsetDuration: fhirtypes.DurationType = Field(
        None,
        alias="offsetDuration",
        title="Time offset for the relationship",
        description=(
            "A duration or range of durations to apply to the relationship. For "
            "example, 30-60 minutes before."
        ),
        # Choice of Data Types. i.e offset[x]
        one_of_many="offset",
        one_of_many_required=False,
    )

    offsetRange: fhirtypes.RangeType = Field(
        None,
        alias="offsetRange",
        title="Time offset for the relationship",
        description=(
            "A duration or range of durations to apply to the relationship. For "
            "example, 30-60 minutes before."
        ),
        # Choice of Data Types. i.e offset[x]
        one_of_many="offset",
        one_of_many_required=False,
    )

    relationship: fhirtypes.Code = Field(
        ...,
        alias="relationship",
        title=(
            "before-start | before | before-end | concurrent-with-start | "
            "concurrent | concurrent-with-end | after-start | after | after-end"
        ),
        description="The relationship of this action to the related action.",
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "before-start",
            "before",
            "before-end",
            "concurrent-with-start",
            "concurrent",
            "concurrent-with-end",
            "after-start",
            "after",
            "after-end",
        ],
    )
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_relationship", title="Extension field for ``relationship``."
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
        one_of_many_fields = {"offset": ["offsetDuration", "offsetRange"]}
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


class PlanDefinitionGoal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    What the plan is trying to accomplish.
    Goals that describe what the activities within the plan are intended to
    achieve. For example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    resource_type = Field("PlanDefinitionGoal", const=True)

    addresses: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="addresses",
        title="What does the goal address",
        description=(
            "Identifies problems, conditions, issues, or concerns the goal is "
            "intended to address."
        ),
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="E.g. Treatment, dietary, behavioral",
        description="Indicates a category the goal falls within.",
    )

    description: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="description",
        title="Code or text describing the goal",
        description=(
            "Human-readable and/or coded description of a specific desired "
            'objective of care, such as "control blood pressure" or "negotiate an '
            'obstacle course" or "dance with child at wedding".'
        ),
    )

    documentation: ListType[fhirtypes.RelatedArtifactType] = Field(
        None,
        alias="documentation",
        title="Supporting documentation for the goal",
        description=(
            "Didactic or other informational resources associated with the goal "
            "that provide further supporting information about the goal. "
            "Information resources can include inline text commentary and links to "
            "web resources."
        ),
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="high-priority | medium-priority | low-priority",
        description=(
            "Identifies the expected level of importance associated with "
            "reaching/sustaining the defined goal."
        ),
    )

    start: fhirtypes.CodeableConceptType = Field(
        None,
        alias="start",
        title="When goal pursuit begins",
        description="The event after which the goal should begin being pursued.",
    )

    target: ListType[fhirtypes.PlanDefinitionGoalTargetType] = Field(
        None,
        alias="target",
        title="Target outcome for the goal",
        description="Indicates what should be done and within what timeframe.",
    )


class PlanDefinitionGoalTarget(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Target outcome for the goal.
    Indicates what should be done and within what timeframe.
    """

    resource_type = Field("PlanDefinitionGoalTarget", const=True)

    detailCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="detailCodeableConcept",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%. Either the high or low or both "
            "values of the range can be specified. When a low value is missing, it "
            "indicates that the goal is achieved at any value at or below the high "
            "value. Similarly, if the high value is missing, it indicates that the "
            "goal is achieved at any value at or above the low value."
        ),
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="detailQuantity",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%. Either the high or low or both "
            "values of the range can be specified. When a low value is missing, it "
            "indicates that the goal is achieved at any value at or below the high "
            "value. Similarly, if the high value is missing, it indicates that the "
            "goal is achieved at any value at or above the low value."
        ),
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    detailRange: fhirtypes.RangeType = Field(
        None,
        alias="detailRange",
        title="The target value to be achieved",
        description=(
            "The target value of the measure to be achieved to signify fulfillment "
            "of the goal, e.g. 150 pounds or 7.0%. Either the high or low or both "
            "values of the range can be specified. When a low value is missing, it "
            "indicates that the goal is achieved at any value at or below the high "
            "value. Similarly, if the high value is missing, it indicates that the "
            "goal is achieved at any value at or above the low value."
        ),
        # Choice of Data Types. i.e detail[x]
        one_of_many="detail",
        one_of_many_required=False,
    )

    due: fhirtypes.DurationType = Field(
        None,
        alias="due",
        title="Reach goal within",
        description=(
            "Indicates the timeframe after the start of the goal in which the goal "
            "should be met."
        ),
    )

    measure: fhirtypes.CodeableConceptType = Field(
        None,
        alias="measure",
        title="The parameter whose value is to be tracked",
        description=(
            "The parameter whose value is to be tracked, e.g. body weight, blood "
            "pressure, or hemoglobin A1c level."
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
            "detail": ["detailCodeableConcept", "detailQuantity", "detailRange"]
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
