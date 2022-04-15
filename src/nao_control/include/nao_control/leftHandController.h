#ifndef LEFT_HAND_CONTROLLER_H_
#define LEFT_HAND_CONTROLLER_H_

#include "jointsController.h"
#include "dispatchEventService.h"
#include "events_def.h"

class LeftHandController: public JointsController{
public:
    LeftHandController();
    ~LeftHandController();
    void start();
    void stop();
    bool handle(const CEvent* ev);

};


#endif