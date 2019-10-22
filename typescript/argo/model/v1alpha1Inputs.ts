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

import { V1alpha1Artifact } from './v1alpha1Artifact';
import { V1alpha1Parameter } from './v1alpha1Parameter';

/**
* Inputs are the mechanism for passing parameters, artifacts, volumes from one template to another
*/
export class V1alpha1Inputs {
    /**
    * Artifact are a list of artifacts passed as inputs
    */
    'artifacts'?: Array<V1alpha1Artifact>;
    /**
    * Parameters are a list of parameters passed as inputs
    */
    'parameters'?: Array<V1alpha1Parameter>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "artifacts",
            "baseName": "artifacts",
            "type": "Array<V1alpha1Artifact>"
        },
        {
            "name": "parameters",
            "baseName": "parameters",
            "type": "Array<V1alpha1Parameter>"
        }    ];

    static getAttributeTypeMap() {
        return V1alpha1Inputs.attributeTypeMap;
    }
}

