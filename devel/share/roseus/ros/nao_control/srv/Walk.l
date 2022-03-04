;; Auto-generated. Do not edit!


(when (boundp 'nao_control::Walk)
  (if (not (find-package "NAO_CONTROL"))
    (make-package "NAO_CONTROL"))
  (shadow 'Walk (find-package "NAO_CONTROL")))
(unless (find-package "NAO_CONTROL::WALK")
  (make-package "NAO_CONTROL::WALK"))
(unless (find-package "NAO_CONTROL::WALKREQUEST")
  (make-package "NAO_CONTROL::WALKREQUEST"))
(unless (find-package "NAO_CONTROL::WALKRESPONSE")
  (make-package "NAO_CONTROL::WALKRESPONSE"))

(in-package "ROS")





(defclass nao_control::WalkRequest
  :super ros::object
  :slots (_joint ))

(defmethod nao_control::WalkRequest
  (:init
   (&key
    ((:joint __joint) "")
    )
   (send-super :init)
   (setq _joint (string __joint))
   self)
  (:joint
   (&optional __joint)
   (if __joint (setq _joint __joint)) _joint)
  (:serialization-length
   ()
   (+
    ;; string _joint
    4 (length _joint)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _joint
       (write-long (length _joint) s) (princ _joint s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _joint
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _joint (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass nao_control::WalkResponse
  :super ros::object
  :slots (_result ))

(defmethod nao_control::WalkResponse
  (:init
   (&key
    ((:result __result) "")
    )
   (send-super :init)
   (setq _result (string __result))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; string _result
    4 (length _result)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _result
       (write-long (length _result) s) (princ _result s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _result
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _result (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass nao_control::Walk
  :super ros::object
  :slots ())

(setf (get nao_control::Walk :md5sum-) "5c2b345790c4d9484fcc900040c864dc")
(setf (get nao_control::Walk :datatype-) "nao_control/Walk")
(setf (get nao_control::Walk :request) nao_control::WalkRequest)
(setf (get nao_control::Walk :response) nao_control::WalkResponse)

(defmethod nao_control::WalkRequest
  (:response () (instance nao_control::WalkResponse :init)))

(setf (get nao_control::WalkRequest :md5sum-) "5c2b345790c4d9484fcc900040c864dc")
(setf (get nao_control::WalkRequest :datatype-) "nao_control/WalkRequest")
(setf (get nao_control::WalkRequest :definition-)
      "string joint 
---
string result

")

(setf (get nao_control::WalkResponse :md5sum-) "5c2b345790c4d9484fcc900040c864dc")
(setf (get nao_control::WalkResponse :datatype-) "nao_control/WalkResponse")
(setf (get nao_control::WalkResponse :definition-)
      "string joint 
---
string result

")



(provide :nao_control/Walk "5c2b345790c4d9484fcc900040c864dc")


