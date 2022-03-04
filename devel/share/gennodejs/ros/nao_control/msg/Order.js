// Auto-generated. Do not edit!

// (in-package nao_control.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Order {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ord = null;
    }
    else {
      if (initObj.hasOwnProperty('ord')) {
        this.ord = initObj.ord
      }
      else {
        this.ord = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Order
    // Serialize message field [ord]
    bufferOffset = _serializer.string(obj.ord, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Order
    let len;
    let data = new Order(null);
    // Deserialize message field [ord]
    data.ord = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.ord.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'nao_control/Order';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2ebdd50f63bd077f07b93a25172b98b2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string ord
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Order(null);
    if (msg.ord !== undefined) {
      resolved.ord = msg.ord;
    }
    else {
      resolved.ord = ''
    }

    return resolved;
    }
};

module.exports = Order;
