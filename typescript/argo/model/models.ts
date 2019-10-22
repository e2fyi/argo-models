export * from './v1alpha1ArchiveStrategy';
export * from './v1alpha1Arguments';
export * from './v1alpha1Artifact';
export * from './v1alpha1ArtifactLocation';
export * from './v1alpha1ArtifactoryArtifact';
export * from './v1alpha1ArtifactoryAuth';
export * from './v1alpha1ContinueOn';
export * from './v1alpha1DAGTask';
export * from './v1alpha1DAGTemplate';
export * from './v1alpha1GitArtifact';
export * from './v1alpha1HDFSArtifact';
export * from './v1alpha1HDFSConfig';
export * from './v1alpha1HDFSKrbConfig';
export * from './v1alpha1HTTPArtifact';
export * from './v1alpha1Inputs';
export * from './v1alpha1Metadata';
export * from './v1alpha1Outputs';
export * from './v1alpha1Parameter';
export * from './v1alpha1RawArtifact';
export * from './v1alpha1ResourceTemplate';
export * from './v1alpha1RetryStrategy';
export * from './v1alpha1S3Artifact';
export * from './v1alpha1S3Bucket';
export * from './v1alpha1ScriptTemplate';
export * from './v1alpha1Sequence';
export * from './v1alpha1Template';
export * from './v1alpha1UserContainer';
export * from './v1alpha1ValueFrom';
export * from './v1alpha1Workflow';
export * from './v1alpha1WorkflowList';
export * from './v1alpha1WorkflowSpec';
export * from './v1alpha1WorkflowStep';

import localVarRequest = require('request');

import { V1alpha1ArchiveStrategy } from './v1alpha1ArchiveStrategy';
import { V1alpha1Arguments } from './v1alpha1Arguments';
import { V1alpha1Artifact } from './v1alpha1Artifact';
import { V1alpha1ArtifactLocation } from './v1alpha1ArtifactLocation';
import { V1alpha1ArtifactoryArtifact } from './v1alpha1ArtifactoryArtifact';
import { V1alpha1ArtifactoryAuth } from './v1alpha1ArtifactoryAuth';
import { V1alpha1ContinueOn } from './v1alpha1ContinueOn';
import { V1alpha1DAGTask } from './v1alpha1DAGTask';
import { V1alpha1DAGTemplate } from './v1alpha1DAGTemplate';
import { V1alpha1GitArtifact } from './v1alpha1GitArtifact';
import { V1alpha1HDFSArtifact } from './v1alpha1HDFSArtifact';
import { V1alpha1HDFSConfig } from './v1alpha1HDFSConfig';
import { V1alpha1HDFSKrbConfig } from './v1alpha1HDFSKrbConfig';
import { V1alpha1HTTPArtifact } from './v1alpha1HTTPArtifact';
import { V1alpha1Inputs } from './v1alpha1Inputs';
import { V1alpha1Metadata } from './v1alpha1Metadata';
import { V1alpha1Outputs } from './v1alpha1Outputs';
import { V1alpha1Parameter } from './v1alpha1Parameter';
import { V1alpha1RawArtifact } from './v1alpha1RawArtifact';
import { V1alpha1ResourceTemplate } from './v1alpha1ResourceTemplate';
import { V1alpha1RetryStrategy } from './v1alpha1RetryStrategy';
import { V1alpha1S3Artifact } from './v1alpha1S3Artifact';
import { V1alpha1S3Bucket } from './v1alpha1S3Bucket';
import { V1alpha1ScriptTemplate } from './v1alpha1ScriptTemplate';
import { V1alpha1Sequence } from './v1alpha1Sequence';
import { V1alpha1Template } from './v1alpha1Template';
import { V1alpha1UserContainer } from './v1alpha1UserContainer';
import { V1alpha1ValueFrom } from './v1alpha1ValueFrom';
import { V1alpha1Workflow } from './v1alpha1Workflow';
import { V1alpha1WorkflowList } from './v1alpha1WorkflowList';
import { V1alpha1WorkflowSpec } from './v1alpha1WorkflowSpec';
import { V1alpha1WorkflowStep } from './v1alpha1WorkflowStep';

/* tslint:disable:no-unused-variable */
let primitives = [
                    "string",
                    "boolean",
                    "double",
                    "integer",
                    "long",
                    "float",
                    "number",
                    "any"
                 ];

let enumsMap: {[index: string]: any} = {
}

let typeMap: {[index: string]: any} = {
    "V1alpha1ArchiveStrategy": V1alpha1ArchiveStrategy,
    "V1alpha1Arguments": V1alpha1Arguments,
    "V1alpha1Artifact": V1alpha1Artifact,
    "V1alpha1ArtifactLocation": V1alpha1ArtifactLocation,
    "V1alpha1ArtifactoryArtifact": V1alpha1ArtifactoryArtifact,
    "V1alpha1ArtifactoryAuth": V1alpha1ArtifactoryAuth,
    "V1alpha1ContinueOn": V1alpha1ContinueOn,
    "V1alpha1DAGTask": V1alpha1DAGTask,
    "V1alpha1DAGTemplate": V1alpha1DAGTemplate,
    "V1alpha1GitArtifact": V1alpha1GitArtifact,
    "V1alpha1HDFSArtifact": V1alpha1HDFSArtifact,
    "V1alpha1HDFSConfig": V1alpha1HDFSConfig,
    "V1alpha1HDFSKrbConfig": V1alpha1HDFSKrbConfig,
    "V1alpha1HTTPArtifact": V1alpha1HTTPArtifact,
    "V1alpha1Inputs": V1alpha1Inputs,
    "V1alpha1Metadata": V1alpha1Metadata,
    "V1alpha1Outputs": V1alpha1Outputs,
    "V1alpha1Parameter": V1alpha1Parameter,
    "V1alpha1RawArtifact": V1alpha1RawArtifact,
    "V1alpha1ResourceTemplate": V1alpha1ResourceTemplate,
    "V1alpha1RetryStrategy": V1alpha1RetryStrategy,
    "V1alpha1S3Artifact": V1alpha1S3Artifact,
    "V1alpha1S3Bucket": V1alpha1S3Bucket,
    "V1alpha1ScriptTemplate": V1alpha1ScriptTemplate,
    "V1alpha1Sequence": V1alpha1Sequence,
    "V1alpha1Template": V1alpha1Template,
    "V1alpha1UserContainer": V1alpha1UserContainer,
    "V1alpha1ValueFrom": V1alpha1ValueFrom,
    "V1alpha1Workflow": V1alpha1Workflow,
    "V1alpha1WorkflowList": V1alpha1WorkflowList,
    "V1alpha1WorkflowSpec": V1alpha1WorkflowSpec,
    "V1alpha1WorkflowStep": V1alpha1WorkflowStep,
}

export class ObjectSerializer {
    public static findCorrectType(data: any, expectedType: string) {
        if (data == undefined) {
            return expectedType;
        } else if (primitives.indexOf(expectedType.toLowerCase()) !== -1) {
            return expectedType;
        } else if (expectedType === "Date") {
            return expectedType;
        } else {
            if (enumsMap[expectedType]) {
                return expectedType;
            }

            if (!typeMap[expectedType]) {
                return expectedType; // w/e we don't know the type
            }

            // Check the discriminator
            let discriminatorProperty = typeMap[expectedType].discriminator;
            if (discriminatorProperty == null) {
                return expectedType; // the type does not have a discriminator. use it.
            } else {
                if (data[discriminatorProperty]) {
                    var discriminatorType = data[discriminatorProperty];
                    if(typeMap[discriminatorType]){
                        return discriminatorType; // use the type given in the discriminator
                    } else {
                        return expectedType; // discriminator did not map to a type
                    }
                } else {
                    return expectedType; // discriminator was not present (or an empty string)
                }
            }
        }
    }

    public static serialize(data: any, type: string) {
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType: string = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData: any[] = [];
            for (let index in data) {
                let date = data[index];
                transformedData.push(ObjectSerializer.serialize(date, subType));
            }
            return transformedData;
        } else if (type === "Date") {
            return data.toISOString();
        } else {
            if (enumsMap[type]) {
                return data;
            }
            if (!typeMap[type]) { // in case we dont know the type
                return data;
            }

            // Get the actual type of this object
            type = this.findCorrectType(data, type);

            // get the map for the correct type.
            let attributeTypes = typeMap[type].getAttributeTypeMap();
            let instance: {[index: string]: any} = {};
            for (let index in attributeTypes) {
                let attributeType = attributeTypes[index];
                instance[attributeType.baseName] = ObjectSerializer.serialize(data[attributeType.name], attributeType.type);
            }
            return instance;
        }
    }

    public static deserialize(data: any, type: string) {
        // polymorphism may change the actual type.
        type = ObjectSerializer.findCorrectType(data, type);
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType: string = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData: any[] = [];
            for (let index in data) {
                let date = data[index];
                transformedData.push(ObjectSerializer.deserialize(date, subType));
            }
            return transformedData;
        } else if (type === "Date") {
            return new Date(data);
        } else {
            if (enumsMap[type]) {// is Enum
                return data;
            }

            if (!typeMap[type]) { // dont know the type
                return data;
            }
            let instance = new typeMap[type]();
            let attributeTypes = typeMap[type].getAttributeTypeMap();
            for (let index in attributeTypes) {
                let attributeType = attributeTypes[index];
                instance[attributeType.name] = ObjectSerializer.deserialize(data[attributeType.baseName], attributeType.type);
            }
            return instance;
        }
    }
}

export interface Authentication {
    /**
    * Apply authentication settings to header and query params.
    */
    applyToRequest(requestOptions: localVarRequest.Options): Promise<void> | void;
}

export class HttpBasicAuth implements Authentication {
    public username: string = '';
    public password: string = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        requestOptions.auth = {
            username: this.username, password: this.password
        }
    }
}

export class ApiKeyAuth implements Authentication {
    public apiKey: string = '';

    constructor(private location: string, private paramName: string) {
    }

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (this.location == "query") {
            (<any>requestOptions.qs)[this.paramName] = this.apiKey;
        } else if (this.location == "header" && requestOptions && requestOptions.headers) {
            requestOptions.headers[this.paramName] = this.apiKey;
        } else if (this.location == 'cookie' && requestOptions && requestOptions.headers) {
            if (requestOptions.headers['Cookie']) {
                requestOptions.headers['Cookie'] += '; ' + this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
            else {
                requestOptions.headers['Cookie'] = this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
        }
    }
}

export class OAuth implements Authentication {
    public accessToken: string = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (requestOptions && requestOptions.headers) {
            requestOptions.headers["Authorization"] = "Bearer " + this.accessToken;
        }
    }
}

export class VoidAuth implements Authentication {
    public username: string = '';
    public password: string = '';

    applyToRequest(_: localVarRequest.Options): void {
        // Do nothing
    }
}