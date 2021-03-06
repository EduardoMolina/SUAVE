## @ingroup Methods-Missions-Segments-Hover
# Hover.py
# 
# Created:  Jan 2016, E. Botero
# Modified:

# ----------------------------------------------------------------------
#  Initialize Conditions
# ----------------------------------------------------------------------

## @ingroup Methods-Missions-Segments-Hover
def initialize_conditions(segment,state):
    """Sets the specified conditions which are given for the segment type.

    Assumptions:
    Descent segment with a constant rate.

    Source:
    N/A

    Inputs:
    segment.altitude                            [meters]
    segment.tim                                 [second]
    state.numerics.dimensionless.control_points [Unitless]
    state.conditions.frames.inertial.time       [seconds]

    Outputs:
    conditions.frames.inertial.velocity_vector  [meters/second]
    conditions.frames.inertial.position_vector  [meters]
    conditions.freestream.altitude              [meters]
    conditions.frames.inertial.time             [seconds]

    Properties Used:
    N/A
    """       
    
    # unpack
    alt        = segment.altitude
    duration   = segment.time
    conditions = state.conditions   
    
    
    # check for initial altitude
    if alt is None:
        if not state.initials: raise AttributeError('altitude not set')
        alt = -1.0 * state.initials.conditions.frames.inertial.position_vector[-1,2]
        segment.altitude = alt        
    
    # dimensionalize time
    t_initial = conditions.frames.inertial.time[0,0]
    t_nondim  = state.numerics.dimensionless.control_points
    time      =  t_nondim * (duration) + t_initial
    
    # pack
    state.conditions.freestream.altitude[:,0]             = alt
    state.conditions.frames.inertial.position_vector[:,2] = -alt # z points down
    state.conditions.frames.inertial.velocity_vector[:,0] = 0.
    state.conditions.frames.inertial.time[:,0]            = time[:,0]    