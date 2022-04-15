#ifndef RIGHT_HAND_CONTROLLER_H_
#define RIGHT_HAND_CONTROLLER_H_


#include "jointsController.h"
#include "dispatchEventService.h"
#include "events_def.h"

class RightHandController: public JointsController{
public:
    RightHandController();
    ~RightHandController();
    void start();
    void stop();
    bool handle(const CEvent* ev);
};


#endif