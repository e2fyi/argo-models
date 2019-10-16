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

import { IoK8sApiCoreV1SecretKeySelector } from './ioK8sApiCoreV1SecretKeySelector';

/**
* S3Artifact is the location of an S3 artifact
*/
export class V1alpha1S3Artifact {
    'accessKeySecret': IoK8sApiCoreV1SecretKeySelector;
    /**
    * Bucket is the name of the bucket
    */
    'bucket': string;
    /**
    * Endpoint is the hostname of the bucket endpoint
    */
    'endpoint': string;
    /**
    * Insecure will connect to the service with TLS
    */
    'insecure'?: boolean;
    /**
    * Key is the key in the bucket where the artifact resides
    */
    'key': string;
    /**
    * Region contains the optional bucket region
    */
    'region'?: string;
    'secretKeySecret': IoK8sApiCoreV1SecretKeySelector;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "accessKeySecret",
            "baseName": "accessKeySecret",
            "type": "IoK8sApiCoreV1SecretKeySelector"
        },
        {
            "name": "bucket",
            "baseName": "bucket",
            "type": "string"
        },
        {
            "name": "endpoint",
            "baseName": "endpoint",
            "type": "string"
        },
        {
            "name": "insecure",
            "baseName": "insecure",
            "type": "boolean"
        },
        {
            "name": "key",
            "baseName": "key",
            "type": "string"
        },
        {
            "name": "region",
            "baseName": "region",
            "type": "string"
        },
        {
            "name": "secretKeySecret",
            "baseName": "secretKeySecret",
            "type": "IoK8sApiCoreV1SecretKeySelector"
        }    ];

    static getAttributeTypeMap() {
        return V1alpha1S3Artifact.attributeTypeMap;
    }
}

