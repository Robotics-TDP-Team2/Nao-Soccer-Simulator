;; Auto-generated. Do not edit!


(when (boundp 'nao_control::Order)
  (if (not (find-package "NAO_CONTROL"))
    (make-package "NAO_CONTROL"))
  (shadow 'Order (find-package "NAO_CONTROL")))
(unless (find-package "NAO_CONTROL::ORDER")
  (make-package "NAO_CONTROL::ORDER"))

(in-package "ROS")
;;//! \htmlinclude Order.msg.html


(defclass nao_control::Order
  :super ros::object
  :slots (_ord ))

(defmethod nao_control::Order
  (:init
   (&key
    ((:ord __ord) "")
    )
   (send-super :init)
   (setq _ord (string __ord))
   self)
  (:ord
   (&optional __ord)
   (if __ord (setq _ord __ord)) _ord)
  (:serialization-length
   ()
   (+
    ;; string _ord
    4 (length _ord)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _ord
       (write-long (length _ord) s) (princ _ord s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _ord
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _ord (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get nao_control::Order :md5sum-) "2ebdd50f63bd077f07b93a25172b98b2")
(setf (get nao_control::Order :datatype-) "nao_control/Order")
(setf (get nao_control::Order :definition-)
      "string ord


")



(provide :nao_control/Order "2ebdd50f63bd077f07b93a25172b98b2")


