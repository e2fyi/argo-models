/**
 * Argo
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2.3.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
* ResourceTemplate is a template subtype to manipulate kubernetes resources
*/
export class V1alpha1ResourceTemplate {
    /**
    * Action is the action to perform to the resource. Must be one of: get, create, apply, delete, replace
    */
    'action': string;
    /**
    * FailureCondition is a label selector expression which describes the conditions of the k8s resource in which the step was considered failed
    */
    'failureCondition'?: string;
    /**
    * Manifest contains the kubernetes manifest
    */
    'manifest': string;
    /**
    * MergeStrategy is the strategy used to merge a patch. It defaults to \"strategic\" Must be one of: strategic, merge, json
    */
    'mergeStrategy'?: string;
    /**
    * SuccessCondition is a label selector expression which describes the conditions of the k8s resource in which it is acceptable to proceed to the following step
    */
    'successCondition'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "action",
            "baseName": "action",
            "type": "string"
        },
        {
            "name": "failureCondition",
            "baseName": "failureCondition",
            "type": "string"
        },
        {
            "name": "manifest",
            "baseName": "manifest",
            "type": "string"
        },
        {
            "name": "mergeStrategy",
            "baseName": "mergeStrategy",
            "type": "string"
        },
        {
            "name": "successCondition",
            "baseName": "successCondition",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return V1alpha1ResourceTemplate.attributeTypeMap;
    }
}

