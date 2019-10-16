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

import { V1alpha1Arguments } from './v1alpha1Arguments';
import { V1alpha1ContinueOn } from './v1alpha1ContinueOn';
import { V1alpha1Sequence } from './v1alpha1Sequence';

/**
* DAGTask represents a node in the graph during DAG execution
*/
export class V1alpha1DAGTask {
    'arguments'?: V1alpha1Arguments;
    'continueOn'?: V1alpha1ContinueOn;
    /**
    * Dependencies are name of other targets which this depends on
    */
    'dependencies'?: Array<string>;
    /**
    * Name is the name of the target
    */
    'name': string;
    /**
    * Name of template to execute
    */
    'template': string;
    /**
    * When is an expression in which the task should conditionally execute
    */
    'when'?: string;
    /**
    * WithItems expands a task into multiple parallel tasks from the items in the list
    */
    'withItems'?: Array<string>;
    /**
    * WithParam expands a task into multiple parallel tasks from the value in the parameter, which is expected to be a JSON list.
    */
    'withParam'?: string;
    'withSequence'?: V1alpha1Sequence;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "arguments",
            "baseName": "arguments",
            "type": "V1alpha1Arguments"
        },
        {
            "name": "continueOn",
            "baseName": "continueOn",
            "type": "V1alpha1ContinueOn"
        },
        {
            "name": "dependencies",
            "baseName": "dependencies",
            "type": "Array<string>"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "template",
            "baseName": "template",
            "type": "string"
        },
        {
            "name": "when",
            "baseName": "when",
            "type": "string"
        },
        {
            "name": "withItems",
            "baseName": "withItems",
            "type": "Array<string>"
        },
        {
            "name": "withParam",
            "baseName": "withParam",
            "type": "string"
        },
        {
            "name": "withSequence",
            "baseName": "withSequence",
            "type": "V1alpha1Sequence"
        }    ];

    static getAttributeTypeMap() {
        return V1alpha1DAGTask.attributeTypeMap;
    }
}

