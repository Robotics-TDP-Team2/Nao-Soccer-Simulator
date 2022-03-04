; Auto-generated. Do not edit!


(cl:in-package nao_control-srv)


;//! \htmlinclude Walk-request.msg.html

(cl:defclass <Walk-request> (roslisp-msg-protocol:ros-message)
  ((joint
    :reader joint
    :initarg :joint
    :type cl:string
    :initform ""))
)

(cl:defclass Walk-request (<Walk-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Walk-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Walk-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nao_control-srv:<Walk-request> is deprecated: use nao_control-srv:Walk-request instead.")))

(cl:ensure-generic-function 'joint-val :lambda-list '(m))
(cl:defmethod joint-val ((m <Walk-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control-srv:joint-val is deprecated.  Use nao_control-srv:joint instead.")
  (joint m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Walk-request>) ostream)
  "Serializes a message object of type '<Walk-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'joint))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'joint))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Walk-request>) istream)
  "Deserializes a message object of type '<Walk-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'joint) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'joint) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Walk-request>)))
  "Returns string type for a service object of type '<Walk-request>"
  "nao_control/WalkRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Walk-request)))
  "Returns string type for a service object of type 'Walk-request"
  "nao_control/WalkRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Walk-request>)))
  "Returns md5sum for a message object of type '<Walk-request>"
  "5c2b345790c4d9484fcc900040c864dc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Walk-request)))
  "Returns md5sum for a message object of type 'Walk-request"
  "5c2b345790c4d9484fcc900040c864dc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Walk-request>)))
  "Returns full string definition for message of type '<Walk-request>"
  (cl:format cl:nil "string joint ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Walk-request)))
  "Returns full string definition for message of type 'Walk-request"
  (cl:format cl:nil "string joint ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Walk-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'joint))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Walk-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Walk-request
    (cl:cons ':joint (joint msg))
))
;//! \htmlinclude Walk-response.msg.html

(cl:defclass <Walk-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:string
    :initform ""))
)

(cl:defclass Walk-response (<Walk-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Walk-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Walk-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name nao_control-srv:<Walk-response> is deprecated: use nao_control-srv:Walk-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <Walk-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader nao_control-srv:result-val is deprecated.  Use nao_control-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Walk-response>) ostream)
  "Serializes a message object of type '<Walk-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'result))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'result))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Walk-response>) istream)
  "Deserializes a message object of type '<Walk-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'result) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'result) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Walk-response>)))
  "Returns string type for a service object of type '<Walk-response>"
  "nao_control/WalkResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Walk-response)))
  "Returns string type for a service object of type 'Walk-response"
  "nao_control/WalkResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Walk-response>)))
  "Returns md5sum for a message object of type '<Walk-response>"
  "5c2b345790c4d9484fcc900040c864dc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Walk-response)))
  "Returns md5sum for a message object of type 'Walk-response"
  "5c2b345790c4d9484fcc900040c864dc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Walk-response>)))
  "Returns full string definition for message of type '<Walk-response>"
  (cl:format cl:nil "string result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Walk-response)))
  "Returns full string definition for message of type 'Walk-response"
  (cl:format cl:nil "string result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Walk-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'result))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Walk-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Walk-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Walk)))
  'Walk-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Walk)))
  'Walk-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Walk)))
  "Returns string type for a service object of type '<Walk>"
  "nao_control/Walk")